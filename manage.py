#!/usr/bin/env python3
"""
Cross-Platform Project Management Script
Replaces manage.sh with Python for Windows/macOS/Linux compatibility
"""

import os
import sys
import platform
import subprocess
import time
import signal
import json
from pathlib import Path
import psutil

class ProjectManager:
    def __init__(self):
        self.project_name = "{{PROJECT_NAME}}"
        self.service_name = "{{SERVICE_NAME}}"
        self.port = "{{PORT}}"
        self.python_command = "{{PYTHON_COMMAND}}"
        self.is_windows = platform.system() == "Windows"
        self.project_root = Path(__file__).parent
        
        # Platform-specific paths
        if self.is_windows:
            self.venv_python = self.project_root / ".venv" / "Scripts" / "python.exe"
            self.venv_pip = self.project_root / ".venv" / "Scripts" / "pip.exe"
        else:
            self.venv_python = self.project_root / ".venv" / "bin" / "python"
            self.venv_pip = self.project_root / ".venv" / "bin" / "pip"
    
    def show_help(self):
        """Display help information"""
        print(f"🚀 {self.project_name} Management")
        print("================================")
        print("")
        print("Commands:")
        print("  setup     - Set up development environment")
        print("  start     - Start service")
        print("  stop      - Stop service")
        print("  restart   - Restart service")
        print("  status    - Check service status")
        print("  logs      - View service logs")
        print("  clean     - Clean up temporary files")
        print("")
        print("Examples:")
        if self.is_windows:
            print("  python manage.py setup")
            print("  python manage.py start")
        else:
            print("  ./manage.py setup")
            print("  ./manage.py start")
    
    def setup_environment(self):
        """Set up development environment"""
        print(f"🔧 Setting up {self.project_name} development environment...")
        
        # Create virtual environment
        venv_dir = self.project_root / ".venv"
        if not venv_dir.exists():
            print("📦 Creating Python virtual environment...")
            subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)
        
        # Install dependencies
        print("📥 Installing dependencies...")
        subprocess.run([str(self.venv_pip), "install", "--upgrade", "pip"], check=True)
        
        requirements_file = self.project_root / "requirements.txt"
        if requirements_file.exists():
            subprocess.run([str(self.venv_pip), "install", "-r", str(requirements_file)], check=True)
        
        # Install cross-platform dependencies
        subprocess.run([str(self.venv_pip), "install", "psutil"], check=True)
        
        # Make scripts executable (Unix only)
        if not self.is_windows:
            print("🔧 Making scripts executable...")
            scripts_dir = self.project_root / "scripts"
            if scripts_dir.exists():
                for script in scripts_dir.glob("*.sh"):
                    script.chmod(0o755)
        
        print("✅ Environment setup complete!")
        print(f"💡 Next: python manage.py start" if self.is_windows else "./manage.py start")
    
    def find_available_port(self, start_port):
        """Find an available port starting from start_port"""
        port = int(start_port)
        max_attempts = 100
        
        for _ in range(max_attempts):
            if not self.is_port_in_use(port):
                return port
            port += 1
        
        print(f"❌ Could not find available port after checking {max_attempts} ports starting from {start_port}")
        sys.exit(1)
    
    def is_port_in_use(self, port):
        """Check if a port is in use using psutil"""
        try:
            connections = psutil.net_connections()
            for conn in connections:
                if conn.laddr.port == port:
                    return True
            return False
        except (psutil.AccessDenied, AttributeError):
            # Fallback method
            import socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                return s.connect_ex(('localhost', port)) == 0
    
    def start_service(self):
        """Start the service"""
        print(f"🚀 Starting {self.service_name}...")
        
        pid_file = self.project_root / f"{self.service_name}.pid"
        
        # Check if already running
        if pid_file.exists():
            try:
                with open(pid_file, 'r') as f:
                    pid = int(f.read().strip())
                
                if psutil.pid_exists(pid):
                    print(f"⚠️  {self.service_name} is already running (PID: {pid})")
                    
                    env_port_file = self.project_root / ".env_port"
                    if env_port_file.exists():
                        with open(env_port_file, 'r') as f:
                            actual_port = f.read().strip()
                        print(f"🌐 Access at: http://localhost:{actual_port}")
                    else:
                        print(f"🌐 Access at: {{{{SERVER_URL}}}}")
                    return
                else:
                    print("🧹 Removing stale PID file")
                    pid_file.unlink()
            except (ValueError, FileNotFoundError):
                pid_file.unlink(missing_ok=True)
        
        # Find available port
        available_port = self.find_available_port(self.port)
        env_port_file = self.project_root / ".env_port"
        
        if available_port != int(self.port):
            print(f"🔄 Port {self.port} is busy, using port {available_port} instead")
            with open(env_port_file, 'w') as f:
                f.write(str(available_port))
        else:
            print(f"✅ Using default port {self.port}")
            env_port_file.unlink(missing_ok=True)
        
        # Set environment variable and start service
        env = os.environ.copy()
        env['PORT'] = str(available_port)
        
        # Start the service
        process = subprocess.Popen(
            [str(self.venv_python), self.python_command],
            cwd=self.project_root,
            env=env
        )
        
        # Save PID
        with open(pid_file, 'w') as f:
            f.write(str(process.pid))
        
        # Wait a moment and verify it started
        time.sleep(2)
        if psutil.pid_exists(process.pid):
            print(f"✅ {self.service_name} started successfully (PID: {process.pid})")
            print(f"🌐 Server: http://localhost:{available_port}")
            print(f"🔍 Health check: http://localhost:{available_port}/health")
        else:
            print(f"❌ Failed to start {self.service_name}")
            pid_file.unlink(missing_ok=True)
            sys.exit(1)
    
    def stop_service(self):
        """Stop the service"""
        print(f"🛑 Stopping {self.service_name}...")
        
        pid_file = self.project_root / f"{self.service_name}.pid"
        
        if pid_file.exists():
            try:
                with open(pid_file, 'r') as f:
                    pid = int(f.read().strip())
                
                if psutil.pid_exists(pid):
                    process = psutil.Process(pid)
                    process.terminate()
                    try:
                        process.wait(timeout=10)
                    except psutil.TimeoutExpired:
                        process.kill()
                    
                    pid_file.unlink()
                    print(f"✅ {self.service_name} stopped")
                else:
                    print(f"⚠️  {self.service_name} was not running")
                    pid_file.unlink()
            except (ValueError, FileNotFoundError, psutil.NoSuchProcess):
                print(f"⚠️  {self.service_name} was not running")
                pid_file.unlink(missing_ok=True)
        else:
            print("⚠️  No PID file found")
    
    def check_status(self):
        """Check service status"""
        # Check port availability
        if self.is_port_in_use(int(self.port)):
            print(f"🔌 Default port {self.port}: In use")
        else:
            print(f"🔌 Default port {self.port}: Available")
        
        # Check service status
        pid_file = self.project_root / f"{self.service_name}.pid"
        
        if pid_file.exists():
            try:
                with open(pid_file, 'r') as f:
                    pid = int(f.read().strip())
                
                if psutil.pid_exists(pid):
                    print(f"✅ {self.service_name} is running (PID: {pid})")
                    
                    env_port_file = self.project_root / ".env_port"
                    if env_port_file.exists():
                        with open(env_port_file, 'r') as f:
                            actual_port = f.read().strip()
                        print(f"🌐 Server: http://localhost:{actual_port}")
                        print(f"🔍 Health check: http://localhost:{actual_port}/health")
                    else:
                        print(f"🌐 Server: {{{{SERVER_URL}}}}")
                        print(f"🔍 Health check: {{{{SERVER_URL}}}}/health")
                else:
                    print(f"❌ {self.service_name} is not running (stale PID file)")
                    pid_file.unlink()
            except (ValueError, FileNotFoundError):
                print(f"❌ {self.service_name} is not running")
        else:
            print(f"❌ {self.service_name} is not running")
    
    def view_logs(self):
        """View service logs"""
        log_file = self.project_root / f"{self.service_name}.log"
        
        if log_file.exists():
            try:
                # Cross-platform tail equivalent
                with open(log_file, 'r') as f:
                    lines = f.readlines()
                    for line in lines[-50:]:  # Show last 50 lines
                        print(line.rstrip())
            except FileNotFoundError:
                print("⚠️  No log file found")
        else:
            print("⚠️  No log file found")
    
    def clean_up(self):
        """Clean up temporary files"""
        print("🧹 Cleaning up temporary files...")
        
        # Remove PID and log files
        for pattern in ["*.pid", "*.log"]:
            for file in self.project_root.glob(pattern):
                file.unlink()
        
        # Remove environment port file
        (self.project_root / ".env_port").unlink(missing_ok=True)
        
        # Remove Python cache directories
        for cache_dir in self.project_root.rglob("__pycache__"):
            import shutil
            shutil.rmtree(cache_dir, ignore_errors=True)
        
        pytest_cache = self.project_root / ".pytest_cache"
        if pytest_cache.exists():
            import shutil
            shutil.rmtree(pytest_cache, ignore_errors=True)
        
        print("✅ Cleanup complete")

def main():
    """Main entry point"""
    manager = ProjectManager()
    
    if len(sys.argv) < 2:
        manager.show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command in ['setup']:
        manager.setup_environment()
    elif command in ['start']:
        manager.start_service()
    elif command in ['stop']:
        manager.stop_service()
    elif command in ['restart']:
        manager.stop_service()
        time.sleep(1)
        manager.start_service()
    elif command in ['status']:
        manager.check_status()
    elif command in ['logs']:
        manager.view_logs()
    elif command in ['clean']:
        manager.clean_up()
    elif command in ['help', '--help', '-h']:
        manager.show_help()
    else:
        print(f"❌ Unknown command: {command}")
        print("")
        manager.show_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
