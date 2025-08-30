#!/usr/bin/env python3
"""
AI Project Inception System - Main Entry Point

This is the orchestrator for the entire AI Project Inception process:
1. Requirements Discovery through intelligent conversation
2. Technology Decision based on requirements analysis  
3. Project Generation with full SDLC automation

Usage:
    python inception.py                    # Start interactive session
    python inception.py --conversation-style list  # Get multiple questions at once
    python inception.py --conversation-style single # One question at a time
"""

import argparse
import sys
from pathlib import Path

# Add inception modules to path
sys.path.insert(0, str(Path(__file__).parent / "inception"))

from discovery.conversation_engine import ConversationEngine
from decision.technology_selector import TechnologySelector
from generation.project_generator import ProjectGenerator

class ProjectInceptionOrchestrator:
    """
    Main orchestrator for the AI Project Inception process
    """
    
    def __init__(self, conversation_style="ask_user"):
        self.conversation_style = conversation_style
        self.conversation_engine = ConversationEngine(style=conversation_style)
        self.technology_selector = TechnologySelector()
        self.project_generator = ProjectGenerator()
        
        # Store the complete project context
        self.project_context = {
            "requirements": {},
            "constraints": {},
            "technology_decisions": {},
            "architecture": {},
            "generated_project": {}
        }
    
    def start_inception(self):
        """
        Main entry point for the AI Project Inception process
        """
        print("🚀 AI Project Inception System")
        print("===============================")
        print("Let's discover what you need to build and create it together!")
        print()
        
        # Phase 1: Requirements Discovery
        print("📋 Phase 1: Requirements Discovery")
        print("----------------------------------")
        requirements = self.conversation_engine.conduct_discovery_interview()
        self.project_context["requirements"] = requirements
        
        # Phase 2: Technology Decision
        print("\n⚙️ Phase 2: Technology Selection")
        print("--------------------------------")
        technology_decisions = self.technology_selector.analyze_and_recommend(requirements)
        self.project_context["technology_decisions"] = technology_decisions
        
        # Phase 3: Project Generation
        print("\n🏗️ Phase 3: Project Generation")
        print("------------------------------")
        generated_project = self.project_generator.create_project(
            requirements, 
            technology_decisions
        )
        self.project_context["generated_project"] = generated_project
        
        # Summary and next steps
        self.display_project_summary()
        return self.project_context
    
    def display_project_summary(self):
        """
        Display a summary of what was created
        """
        print("\n🎉 Project Inception Complete!")
        print("==============================")
        
        tech = self.project_context["technology_decisions"]
        project = self.project_context["generated_project"]
        
        print(f"📁 Project: {project.get('name', 'Your Project')}")
        print(f"🏗️ Type: {tech.get('project_type', 'Unknown')}")
        print(f"💻 Technology: {tech.get('tech_stack', 'Unknown')}")
        print(f"📍 Location: {project.get('path', 'Unknown')}")
        print()
        print("Next steps:")
        print(f"1. cd {project.get('path', 'your-project')}")
        print("2. Follow the setup instructions in README.md")
        print("3. Start coding with full SDLC automation!")

def main():
    """
    Command line interface for the AI Project Inception System
    """
    parser = argparse.ArgumentParser(
        description="AI Project Inception System - From Requirements to Working Project"
    )
    
    parser.add_argument(
        "--conversation-style",
        choices=["ask_user", "single", "list"],
        default="ask_user",
        help="How to conduct the discovery conversation (default: ask_user for preference)"
    )
    
    parser.add_argument(
        "--output-dir",
        type=str,
        default="./generated_projects",
        help="Directory where generated projects will be created"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output for debugging"
    )
    
    args = parser.parse_args()
    
    try:
        # Initialize and run the inception process
        orchestrator = ProjectInceptionOrchestrator(
            conversation_style=args.conversation_style
        )
        
        project_context = orchestrator.start_inception()
        
        if args.verbose:
            print("\n🔍 Complete Project Context:")
            print("============================")
            import json
            print(json.dumps(project_context, indent=2))
            
        return 0
        
    except KeyboardInterrupt:
        print("\n\n👋 Project inception cancelled by user.")
        return 1
    except Exception as e:
        print(f"\n❌ Error during project inception: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
