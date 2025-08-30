"""
AI Project Inception - Conversation Engine

Handles intelligent requirements discovery through structured conversations.
Adapts questioning based on user responses and project complexity.
"""

import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum

class ConversationStyle(Enum):
    SINGLE = "single"  # One question at a time
    LIST = "list"      # Multiple questions at once
    ADAPTIVE = "adaptive"  # Smart adaptation based on responses

@dataclass
class UserResponse:
    """Represents a user response with metadata"""
    question_id: str
    question: str
    answer: str
    confidence: float = 1.0  # How confident we are in understanding the answer
    needs_clarification: bool = False

class ConversationEngine:
    """
    Manages the requirements discovery conversation process
    """
    
    def __init__(self, style: str = "adaptive"):
        self.style = ConversationStyle(style) if style != "ask_user" else None
        self.conversation_history: List[UserResponse] = []
        self.requirements: Dict[str, Any] = {
            "project_goal": "",
            "user_context": {},
            "technical_context": {},
            "constraints": {},
            "success_criteria": {}
        }
        
        # Question libraries for different discovery areas
        self.question_libraries = self._load_question_libraries()
    
    def _load_question_libraries(self) -> Dict[str, List[Dict]]:
        """
        Load structured question libraries for different discovery areas
        """
        return {
            "initial": [
                {
                    "id": "project_goal",
                    "question": "What problem are you trying to solve or what do you want to build?",
                    "type": "open_text",
                    "required": True,
                    "follow_up": True
                }
            ],
            "user_context": [
                {
                    "id": "team_size",
                    "question": "How many people are on your team?",
                    "type": "number",
                    "range": [1, 1000],
                    "follow_up_triggers": {
                        "1": ["solo_developer_questions"],
                        ">10": ["large_team_questions"]
                    }
                },
                {
                    "id": "team_roles",
                    "question": "What roles do people on your team have? (e.g., engineers, designers, PMs, etc.)",
                    "type": "open_text",
                    "condition": lambda ctx: ctx.get("team_size", 1) > 1
                },
                {
                    "id": "technical_comfort",
                    "question": "How would you rate your team's technical comfort level?",
                    "type": "choice",
                    "options": ["Beginner", "Intermediate", "Advanced", "Expert"],
                    "required": True
                },
                {
                    "id": "end_users",
                    "question": "Who are the end users of this solution? (team members, customers, public, etc.)",
                    "type": "open_text",
                    "required": True
                }
            ],
            "technical_context": [
                {
                    "id": "existing_tools",
                    "question": "What tools and systems does your team currently use?",
                    "type": "open_text",
                    "examples": ["Slack, Jira, GitHub, AWS, Google Workspace, etc."]
                },
                {
                    "id": "integration_needs",
                    "question": "Does this need to integrate with any existing systems?",
                    "type": "open_text",
                    "follow_up": True
                },
                {
                    "id": "deployment_preference",
                    "question": "Where would you prefer to run this?",
                    "type": "choice",
                    "options": ["Local/On-premise", "Cloud (AWS/GCP/Azure)", "No preference", "Don't know"]
                },
                {
                    "id": "access_patterns",
                    "question": "How will people access this solution?",
                    "type": "choice",
                    "options": ["Web browser", "Mobile app", "Command line", "Desktop app", "API/Integration", "Multiple ways"]
                }
            ],
            "constraints": [
                {
                    "id": "timeline",
                    "question": "What's your timeline for getting this working?",
                    "type": "choice",
                    "options": ["This week", "Within 2 weeks", "Within a month", "2-3 months", "No rush"]
                },
                {
                    "id": "budget",
                    "question": "What's your budget situation?",
                    "type": "choice",
                    "options": ["Minimal cost (free/open source)", "Small budget ($10-100/month)", "Medium budget ($100-500/month)", "Flexible budget"]
                },
                {
                    "id": "maintenance",
                    "question": "Who will maintain this solution long-term?",
                    "type": "open_text"
                },
                {
                    "id": "scalability",
                    "question": "How many users do you expect this to serve?",
                    "type": "choice",
                    "options": ["Just my team (1-20)", "Department (20-100)", "Company (100-1000)", "Public/Many users (1000+)"]
                }
            ],
            "success_criteria": [
                {
                    "id": "success_definition",
                    "question": "How will you know this project is successful?",
                    "type": "open_text",
                    "required": True
                },
                {
                    "id": "must_have_features",
                    "question": "What features are absolutely essential for the first version?",
                    "type": "open_text",
                    "required": True
                },
                {
                    "id": "nice_to_have",
                    "question": "What features would be nice to have but aren't critical?",
                    "type": "open_text"
                }
            ]
        }
    
    def conduct_discovery_interview(self) -> Dict[str, Any]:
        """
        Main method to conduct the requirements discovery interview
        """
        print("I'll ask you some questions to understand what you need to build.")
        
        # Ask about conversation style if not specified
        if self.style is None:
            self.style = self._ask_conversation_preference()
        
        print(f"\nGreat! I'll {self._get_style_description()}")
        print()
        
        # Conduct the interview by category
        self._ask_category("initial", "First, let's understand your goal:")
        
        # Analyze initial response to determine follow-up focus
        project_goal = self.requirements.get("project_goal", "")
        follow_up_categories = self._determine_follow_up_categories(project_goal)
        
        # Ask follow-up questions based on project type
        for category in follow_up_categories:
            category_title = category.replace("_", " ").title()
            self._ask_category(category, f"\nNow, let's talk about {category_title.lower()}:")
        
        # Final clarification round
        self._clarification_round()
        
        return self.requirements
    
    def _ask_conversation_preference(self) -> ConversationStyle:
        """
        Ask user how they prefer to have the conversation
        """
        print("How would you like me to ask you questions?")
        print("1. One question at a time (more conversational)")
        print("2. Give me a list of questions to answer at once (faster)")
        print("3. Let you decide as we go (adaptive)")
        
        while True:
            choice = input("\nYour preference (1-3): ").strip()
            if choice == "1":
                return ConversationStyle.SINGLE
            elif choice == "2":
                return ConversationStyle.LIST
            elif choice == "3":
                return ConversationStyle.ADAPTIVE
            else:
                print("Please enter 1, 2, or 3")
    
    def _get_style_description(self) -> str:
        """
        Get a description of the chosen conversation style
        """
        if self.style == ConversationStyle.SINGLE:
            return "ask you one question at a time."
        elif self.style == ConversationStyle.LIST:
            return "give you groups of related questions to answer together."
        else:
            return "adapt my questioning style based on your responses."
    
    def _ask_category(self, category: str, intro: str):
        """
        Ask questions from a specific category
        """
        print(intro)
        questions = self.question_libraries.get(category, [])
        
        if self.style == ConversationStyle.LIST:
            self._ask_questions_as_list(questions, category)
        else:
            self._ask_questions_individually(questions, category)
    
    def _ask_questions_individually(self, questions: List[Dict], category: str):
        """
        Ask questions one by one
        """
        for question_data in questions:
            if self._should_ask_question(question_data):
                answer = self._ask_single_question(question_data)
                self._process_answer(question_data, answer, category)
    
    def _ask_questions_as_list(self, questions: List[Dict], category: str):
        """
        Present multiple questions at once for batch answering
        """
        applicable_questions = [q for q in questions if self._should_ask_question(q)]
        
        if not applicable_questions:
            return
        
        print(f"\nHere are some questions about {category.replace('_', ' ')}:")
        for i, q in enumerate(applicable_questions, 1):
            print(f"{i}. {q['question']}")
            if q.get('examples'):
                print(f"   Examples: {', '.join(q['examples'])}")
        
        print("\nYou can answer with just the numbers (e.g., '1. Answer here, 2. Another answer...')")
        print("Or just answer in order, separated by newlines:")
        
        response = input("\nYour answers:\n").strip()
        answers = self._parse_batch_response(response, applicable_questions)
        
        for question_data, answer in zip(applicable_questions, answers):
            if answer:
                self._process_answer(question_data, answer, category)
    
    def _ask_single_question(self, question_data: Dict) -> str:
        """
        Ask a single question and get the response
        """
        question = question_data["question"]
        
        if question_data.get("type") == "choice":
            options = question_data.get("options", [])
            print(f"\n{question}")
            for i, option in enumerate(options, 1):
                print(f"  {i}. {option}")
            
            while True:
                choice = input("Your choice (number or text): ").strip()
                if choice.isdigit() and 1 <= int(choice) <= len(options):
                    return options[int(choice) - 1]
                elif choice in options:
                    return choice
                else:
                    # Allow free text for flexibility
                    return choice
        else:
            if question_data.get("examples"):
                print(f"\n{question}")
                print(f"Examples: {', '.join(question_data['examples'])}")
            else:
                print(f"\n{question}")
            
            return input("Your answer: ").strip()
    
    def _should_ask_question(self, question_data: Dict) -> bool:
        """
        Determine if a question should be asked based on conditions
        """
        condition = question_data.get("condition")
        if condition and callable(condition):
            return condition(self.requirements)
        return True
    
    def _process_answer(self, question_data: Dict, answer: str, category: str):
        """
        Process and store a question answer
        """
        question_id = question_data["id"]
        
        # Store the answer
        if category not in self.requirements:
            self.requirements[category] = {}
        
        self.requirements[category][question_id] = answer
        
        # Also store at top level for easy access
        self.requirements[question_id] = answer
        
        # Record conversation history
        self.conversation_history.append(UserResponse(
            question_id=question_id,
            question=question_data["question"],
            answer=answer
        ))
        
        # Handle follow-up triggers
        self._handle_follow_up_triggers(question_data, answer)
    
    def _handle_follow_up_triggers(self, question_data: Dict, answer: str):
        """
        Handle any follow-up questions triggered by this answer
        """
        triggers = question_data.get("follow_up_triggers", {})
        
        for trigger_condition, follow_up_categories in triggers.items():
            if self._check_trigger_condition(trigger_condition, answer):
                for category in follow_up_categories:
                    # Add follow-up questions (this is a simplified implementation)
                    print(f"  → That triggers some follow-up questions about {category}")
    
    def _check_trigger_condition(self, condition: str, answer: str) -> bool:
        """
        Check if a trigger condition is met
        """
        if condition.startswith(">"):
            try:
                threshold = int(condition[1:])
                return int(answer) > threshold
            except ValueError:
                return False
        elif condition.startswith("<"):
            try:
                threshold = int(condition[1:])
                return int(answer) < threshold
            except ValueError:
                return False
        else:
            return condition.lower() in answer.lower()
    
    def _parse_batch_response(self, response: str, questions: List[Dict]) -> List[str]:
        """
        Parse a batch response into individual answers
        """
        # Simple implementation - split by newlines or numbered format
        lines = [line.strip() for line in response.split('\n') if line.strip()]
        
        # If user used numbered format, extract answers
        if any(line.startswith(f"{i}.") for i, line in enumerate(lines, 1)):
            answers = []
            for i in range(len(questions)):
                for line in lines:
                    if line.startswith(f"{i+1}."):
                        answers.append(line[line.find('.') + 1:].strip())
                        break
                else:
                    answers.append("")
            return answers
        else:
            # Assume answers are in order, one per line
            return lines + [""] * (len(questions) - len(lines))
    
    def _determine_follow_up_categories(self, project_goal: str) -> List[str]:
        """
        Determine which follow-up question categories to ask based on initial goal
        """
        # Simple keyword-based categorization (could be much more sophisticated)
        categories = ["user_context", "technical_context", "constraints", "success_criteria"]
        
        # All categories for now, but could be smart about this
        return categories
    
    def _clarification_round(self):
        """
        Final round to clarify any ambiguous or incomplete answers
        """
        print("\n🔍 Quick clarification round:")
        
        # Check for any answers that might need clarification
        needs_clarification = [
            resp for resp in self.conversation_history 
            if resp.needs_clarification or len(resp.answer) < 5
        ]
        
        if needs_clarification:
            print("Let me clarify a few things:")
            for resp in needs_clarification[:3]:  # Limit to 3 clarifications
                print(f"\nEarlier you said '{resp.answer}' for: {resp.question}")
                clarification = input("Could you expand on that a bit? ").strip()
                if clarification:
                    # Update the answer
                    resp.answer = f"{resp.answer}. {clarification}"
                    self.requirements[resp.question_id] = resp.answer
        else:
            print("Everything looks clear! Moving on to technology selection...")

    def get_conversation_summary(self) -> str:
        """
        Generate a summary of the conversation for the technology selector
        """
        summary = []
        summary.append(f"Project Goal: {self.requirements.get('project_goal', 'Not specified')}")
        
        for category in ["user_context", "technical_context", "constraints", "success_criteria"]:
            if category in self.requirements:
                summary.append(f"\n{category.title()}:")
                for key, value in self.requirements[category].items():
                    summary.append(f"  {key}: {value}")
        
        return "\n".join(summary)
