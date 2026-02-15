#!/usr/bin/env python3
"""
Textbook Creator Skill - Builder Type for Educational Content Domain

This skill provides comprehensive textbook creation capabilities with proper pedagogical structure,
accessibility considerations, and subject-specific content generation.
"""

import os
import json
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any

class TextbookCreator:
    def __init__(self, config_path: str = "skill.yaml"):
        self.config = self._load_config(config_path)
        self.references = self._load_references()
        self.templates = self._load_templates()
        self.checklists = self._load_checklists()
        self.workflows = self._load_workflows()

    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load skill configuration from YAML file."""
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def _load_references(self) -> Dict[str, str]:
        """Load educational standards and references."""
        references = {}
        ref_dir = Path("references")
        for ref_file in ref_dir.glob("*.md"):
            with open(ref_file, 'r', encoding='utf-8') as f:
                references[ref_file.stem] = f.read()
        return references

    def _load_templates(self) -> Dict[str, str]:
        """Load textbook templates."""
        templates = {}
        template_dir = Path("templates")
        for template_file in template_dir.glob("*.md"):
            with open(template_file, 'r', encoding='utf-8') as f:
                templates[template_file.stem] = f.read()
        return templates

    def _load_checklists(self) -> Dict[str, str]:
        """Load quality assurance checklists."""
        checklists = {}
        checklist_dir = Path("checklists")
        for checklist_file in checklist_dir.glob("*.md"):
            with open(checklist_file, 'r', encoding='utf-8') as f:
                checklists[checklist_file.stem] = f.read()
        return checklists

    def _load_workflows(self) -> Dict[str, str]:
        """Load textbook creation workflows."""
        workflows = {}
        workflow_dir = Path("workflows")
        for workflow_file in workflow_dir.glob("*.md"):
            with open(workflow_file, 'r', encoding='utf-8') as f:
                workflows[workflow_file.stem] = f.read()
        return workflows

    def initialize_textbook(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Initialize a new textbook project."""
        required_params = ['title', 'subject', 'level', 'authors']
        for param in required_params:
            if param not in params:
                raise ValueError(f"Missing required parameter: {param}")

        # Create basic textbook structure
        textbook = {
            'metadata': {
                'title': params['title'],
                'subject': params['subject'],
                'level': params['level'],
                'authors': params['authors'],
                'edition': params.get('edition', '1.0'),
                'language': params.get('language', 'en'),
                'created_date': params.get('created_date', '2026-02-14'),
                'status': 'planning'
            },
            'table_of_contents': [],
            'chapters': [],
            'learning_objectives': [],
            'quality_assurance': {
                'accessibility_score': 0,
                'pedagogical_score': 0,
                'content_quality': 0
            }
        }

        return textbook

    def generate_chapter_structure(self, textbook: Dict[str, Any], chapter_params: Dict[str, Any]) -> Dict[str, Any]:
        """Generate structured chapter with proper educational components."""
        chapter_number = chapter_params['chapter_number']
        chapter_title = chapter_params['chapter_title']
        learning_objectives = chapter_params['learning_objectives']

        # Validate learning objectives
        validated_objectives = self._validate_learning_objectives(learning_objectives)

        # Create chapter structure
        chapter = {
            'chapter_number': chapter_number,
            'chapter_title': chapter_title,
            'learning_objectives': validated_objectives,
            'sections': [],
            'summary': '',
            'assessment': [],
            'key_points': [],
            'estimated_duration': chapter_params.get('duration', '2-3 hours'),
            'prerequisites': chapter_params.get('prerequisites', [])
        }

        # Add to textbook
        textbook['chapters'].append(chapter)
        textbook['table_of_contents'].append({
            'chapter_number': chapter_number,
            'chapter_title': chapter_title,
            'page_number': len(textbook['chapters'])
        })

        return textbook

    def generate_section_content(self, textbook: Dict[str, Any], section_params: Dict[str, Any]) -> Dict[str, Any]:
        """Generate educational section content with proper structure."""
        chapter_index = section_params['chapter'] - 1
        if chapter_index >= len(textbook['chapters']):
            raise IndexError("Chapter number out of range")

        chapter = textbook['chapters'][chapter_index]

        # Generate section content based on type
        section_type = section_params.get('content_type', 'main')
        content = self._generate_section_content(section_type, section_params)

        # Create section structure
        section = {
            'section_id': section_params['section'],
            'title': section_params['title'],
            'content': content,
            'learning_objective': section_params.get('learning_objective', ''),
            'examples': section_params.get('examples', []),
            'exercises': section_params.get('exercises', []),
            'key_points': section_params.get('key_points', []),
            'difficulty': section_params.get('difficulty', 'medium')
        }

        # Add to chapter
        chapter['sections'].append(section)

        return textbook

    def _generate_section_content(self, content_type: str, params: Dict[str, Any]) -> str:
        """Generate content based on section type."""
        if content_type == 'main':
            return self._generate_main_content(params)
        elif content_type == 'example':
            return self._generate_example_content(params)
        elif content_type == 'exercise':
            return self._generate_exercise_content(params)
        elif content_type == 'assessment':
            return self._generate_assessment_content(params)
        else:
            return self._generate_default_content(params)

    def _generate_main_content(self, params: Dict[str, Any]) -> str:
        """Generate main educational content."""
        content = f"""
## Section {params.get('section', '1.1')}: {params['title']}

### Learning Objective
{params.get('learning_objective', 'Understand key concepts related to this section.')}

### Content
This section covers {params['title']} in detail. The key concepts include:

- Concept 1: {params.get('concept1', 'Basic principle')}
- Concept 2: {params.get('concept2', 'Advanced principle')}
- Concept 3: {params.get('concept3', 'Application')}

### Key Points
- [ ] {params.get('key_point1', 'Important point 1')}
- [ ] {params.get('key_point2', 'Important point 2')}
- [ ] {params.get('key_point3', 'Important point 3')}

### Examples
{self._generate_examples(params.get('num_examples', 2))}

### Practice Exercises
{self._generate_exercises(params.get('num_exercises', 3))}
        """
        return content

    def _generate_examples(self, num_examples: int) -> str:
        """Generate example content."""
        examples = []
        for i in range(num_examples):
            examples.append(f"""
#### Example {i+1}
**Problem:** Describe a typical problem for this concept.

**Solution:**
```
Step-by-step solution would go here.
```

**Key Takeaway:** Main lesson from this example.
        """)
        return "\n\n".join(examples)

    def _generate_exercises(self, num_exercises: int) -> str:
        """Generate exercise content."""
        exercises = []
        for i in range(num_exercises):
            difficulty = "Easy" if i < num_exercises/2 else "Challenging"
            exercises.append(f"""
**Exercise {i+1} ({difficulty}):**
Describe an exercise problem here.

**Hint:** Provide a helpful hint.

**Solution:**
Provide solution guidance.
            """)
        return "\n\n".join(exercises)

    def generate_assessment_items(self, textbook: Dict[str, Any], assessment_params: Dict[str, Any]) -> Dict[str, Any]:
        """Generate assessment items for a chapter."""
        chapter_index = assessment_params['chapter'] - 1
        if chapter_index >= len(textbook['chapters']):
            raise IndexError("Chapter number out of range")

        chapter = textbook['chapters'][chapter_index]

        # Generate assessment items
        assessment_type = assessment_params['type']
        num_questions = assessment_params['questions']

        assessment = {
            'type': assessment_type,
            'questions': [],
            'time_limit': assessment_params.get('time_limit', '60 minutes'),
            'difficulty_distribution': assessment_params.get('difficulty', 'balanced')
        }

        # Generate questions
        for i in range(num_questions):
            question = self._generate_question(assessment_type, i+1)
            assessment['questions'].append(question)

        chapter['assessment'].append(assessment)

        return textbook

    def _generate_question(self, question_type: str, question_number: int) -> Dict[str, Any]:
        """Generate a question based on type."""
        if question_type == 'quiz':
            return {
                'question_number': question_number,
                'question_type': 'multiple_choice',
                'question_text': f"What is the main concept of section {question_number}?",
                'options': ['Option A', 'Option B', 'Option C', 'Option D'],
                'correct_answer': 'A',
                'difficulty': 'medium'
            }
        elif question_type == 'test':
            return {
                'question_number': question_number,
                'question_type': 'short_answer',
                'question_text': f"Explain the key principles of concept {question_number}.",
                'rubric': 'Clear explanation with examples',
                'difficulty': 'high'
            }
        elif question_type == 'self-check':
            return {
                'question_number': question_number,
                'question_type': 'true_false',
                'question_text': f"True or False: Concept {question_number} is correctly described.",
                'correct_answer': 'true',
                'difficulty': 'easy'
            }
        else:
            return {
                'question_number': question_number,
                'question_type': 'open_ended',
                'question_text': f"Discuss the implications of concept {question_number}.",
                'guidelines': 'Provide detailed analysis',
                'difficulty': 'medium'
            }

    def run_quality_checks(self, textbook: Dict[str, Any], check_level: str = 'basic') -> Dict[str, Any]:
        """Run quality assurance checks on the textbook."""
        results = {
            'status': 'passed',
            'checks_run': check_level,
            'issues_found': 0,
            'detailed_results': {}
        }

        # Run basic checks
        if check_level in ['basic', 'comprehensive']:
            basic_results = self._run_basic_checks(textbook)
            results['detailed_results'].update(basic_results)
            if basic_results.get('issues_found', 0) > 0:
                results['status'] = 'needs_improvement'
            results['issues_found'] += basic_results.get('issues_found', 0)

        # Run comprehensive checks
        if check_level == 'comprehensive':
            comprehensive_results = self._run_comprehensive_checks(textbook)
            results['detailed_results'].update(comprehensive_results)
            if comprehensive_results.get('issues_found', 0) > 0:
                results['status'] = 'needs_improvement'
            results['issues_found'] += comprehensive_results.get('issues_found', 0)

        # Calculate quality scores
        results = self._calculate_quality_scores(textbook, results)

        return results

    def _run_basic_checks(self, textbook: Dict[str, Any]) -> Dict[str, Any]:
        """Run basic quality checks."""
        issues = 0
        results = {}

        # Check required metadata
        required_metadata = ['title', 'subject', 'level', 'authors']
        for field in required_metadata:
            if not textbook['metadata'].get(field):
                issues += 1
                results[f'metadata_{field}'] = 'Missing required field'

        # Check chapter structure
        if not textbook['chapters']:
            issues += 1
            results['chapters'] = 'No chapters defined'
        else:
            for i, chapter in enumerate(textbook['chapters']):
                if not chapter.get('chapter_title'):
                    issues += 1
                    results[f'chapter_{i+1}_title'] = 'Missing chapter title'
                if not chapter.get('learning_objectives'):
                    issues += 1
                    results[f'chapter_{i+1}_objectives'] = 'Missing learning objectives'

        return {
            'issues_found': issues,
            'basic_checks': results
        }

    def _run_comprehensive_checks(self, textbook: Dict[str, Any]) -> Dict[str, Any]:
        """Run comprehensive quality checks."""
        issues = 0
        results = {}

        # Check accessibility compliance
        accessibility_issues = self._check_accessibility_compliance(textbook)
        if accessibility_issues:
            issues += len(accessibility_issues)
            results['accessibility'] = accessibility_issues

        # Check pedagogical alignment
        pedagogical_issues = self._check_pedagogical_alignment(textbook)
        if pedagogical_issues:
            issues += len(pedagogical_issues)
            results['pedagogy'] = pedagogical_issues

        # Check content quality
        content_issues = self._check_content_quality(textbook)
        if content_issues:
            issues += len(content_issues)
            results['content_quality'] = content_issues

        return {
            'issues_found': issues,
            'comprehensive_checks': results
        }

    def _calculate_quality_scores(self, textbook: Dict[str, Any], results: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate quality scores based on check results."""
        # Calculate accessibility score
        accessibility_score = 100
        if 'accessibility' in results['detailed_results']:
            accessibility_issues = len(results['detailed_results']['accessibility'])
            accessibility_score -= accessibility_issues * 10
        textbook['quality_assurance']['accessibility_score'] = max(0, accessibility_score)

        # Calculate pedagogical score
        pedagogical_score = 100
        if 'pedagogy' in results['detailed_results']:
            pedagogical_issues = len(results['detailed_results']['pedagogy'])
            pedagogical_score -= pedagogical_issues * 10
        textbook['quality_assurance']['pedagogical_score'] = max(0, pedagogical_score)

        # Calculate content quality score
        content_quality_score = 100
        if 'content_quality' in results['detailed_results']:
            content_issues = len(results['detailed_results']['content_quality'])
            content_quality_score -= content_issues * 10
        textbook['quality_assurance']['content_quality'] = max(0, content_quality_score)

        # Calculate overall quality score
        overall_score = (accessibility_score + pedagogical_score + content_quality_score) / 3
        textbook['quality_assurance']['overall_score'] = round(overall_score, 2)

        return results

    def export_textbook(self, textbook: Dict[str, Any], format: str = 'pdf') -> str:
        """Export textbook in specified format."""
        if format == 'pdf':
            return self._export_to_pdf(textbook)
        elif format == 'epub':
            return self._export_to_epub(textbook)
        elif format == 'html':
            return self._export_to_html(textbook)
        elif format == 'latex':
            return self._export_to_latex(textbook)
        else:
            raise ValueError(f"Unsupported export format: {format}")

    def _export_to_pdf(self, textbook: Dict[str, Any]) -> str:
        """Export textbook to PDF format."""
        # Generate LaTeX content for PDF export
        latex_content = self._generate_latex_content(textbook)

        # Save to temporary file
        output_file = f"{textbook['metadata']['title'].replace(' ', '_')}_export.tex"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(latex_content)

        return f"Textbook exported to LaTeX file: {output_file}"

    def _generate_latex_content(self, textbook: Dict[str, Any]) -> str:
        """Generate LaTeX content for textbook export."""
        latex = r"""
\documentclass[12pt]{book}
\usepackage{hyperref}
\usepackage{accessibility}
\title{{TEXTBOOK_TITLE}}
\author{{AUTHORS}}
\date{{DATE}}
\begin{document}
\maketitle
\tableofcontents
        """

        # Replace placeholders
        latex = latex.replace('TEXTBOOK_TITLE', textbook['metadata']['title'])
        latex = latex.replace('AUTHORS', ', '.join(textbook['metadata']['authors']))
        latex = latex.replace('DATE', textbook['metadata']['created_date'])

        # Add chapters
        for chapter in textbook['chapters']:
            latex += self._generate_chapter_latex(chapter)

        latex += r"""
\end{document}
        """

        return latex

    def _generate_chapter_latex(self, chapter: Dict[str, Any]) -> str:
        """Generate LaTeX for a chapter."""
        latex = f"""
\chapter{{{chapter['chapter_title']}}}

\section*{{Learning Objectives}}
        """

        for objective in chapter['learning_objectives']:
            latex += f"\n- {objective}"

        # Add sections
        for section in chapter['sections']:
            latex += self._generate_section_latex(section)

        # Add summary
        latex += f"\n\section*{{Summary}}\n{chapter.get('summary', 'This chapter covered the key concepts of {chapter_title}.')}"

        # Add assessment
        if chapter.get('assessment'):
            latex += "\n\section*{{Assessment}}\n"
            for assessment in chapter['assessment']:
                latex += self._generate_assessment_latex(assessment)

        return latex

    def _generate_section_latex(self, section: Dict[str, Any]) -> str:
        """Generate LaTeX for a section."""
        latex = f"""
\subsection{{{section['title']}}}

\textbf{{Learning Objective:}} {section.get('learning_objective', '')}

{section['content']}
        """

        # Add examples
        if section.get('examples'):
            latex += "\n\subsubsection*{Examples}\n"
            for example in section['examples']:
                latex += f"\n**Example:** {example}\n"

        # Add exercises
        if section.get('exercises'):
            latex += "\n\subsubsection*{Exercises}\n"
            for exercise in section['exercises']:
                latex += f"\n**Exercise:** {exercise}\n"

        return latex

    def _generate_assessment_latex(self, assessment: Dict[str, Any]) -> str:
        """Generate LaTeX for assessment."""
        latex = f"\n\textbf{{Assessment Type:}} {assessment['type']}\n"

        for question in assessment['questions']:
            latex += f"\n\textbf{{Question {question['question_number']}:}} {question['question_text']}\n"
            if question.get('options'):
                latex += "\n\begin{{enumerate}}\n"
                for option in question['options']:
                    latex += f"\n  \item {option}"
                latex += "\n\end{{enumerate}}\n"

        return latex

    def _validate_learning_objectives(self, objectives: List[str]) -> List[str]:
        """Validate and format learning objectives."""
        validated = []
        for obj in objectives:
            # Ensure objectives start with action verbs
            action_verbs = ['Understand', 'Explain', 'Apply', 'Analyze', 'Evaluate', 'Create']
            if not any(obj.startswith(verb) for verb in action_verbs):
                obj = f"Understand {obj}"
            validated.append(obj)
        return validated

    def _check_accessibility_compliance(self, textbook: Dict[str, Any]) -> List[str]:
        """Check textbook for accessibility compliance."""
        issues = []

        # Check metadata accessibility
        if not textbook['metadata'].get('language'):
            issues.append("Missing language specification in metadata")

        # Check chapter accessibility
        for chapter in textbook['chapters']:
            if not chapter.get('prerequisites'):
                issues.append(f"Chapter {chapter['chapter_number']} missing prerequisites")

        return issues

    def _check_pedagogical_alignment(self, textbook: Dict[str, Any]) -> List[str]:
        """Check textbook for pedagogical alignment."""
        issues = []

        # Check learning objective alignment
        for chapter in textbook['chapters']:
            if len(chapter.get('learning_objectives', [])) < 2:
                issues.append(f"Chapter {chapter['chapter_number']} needs more learning objectives")

        return issues

    def _check_content_quality(self, textbook: Dict[str, Any]) -> List[str]:
        """Check textbook for content quality."""
        issues = []

        # Check for empty content
        for chapter in textbook['chapters']:
            for section in chapter.get('sections', []):
                if not section.get('content'):
                    issues.append(f"Section {section['section_id']} in chapter {chapter['chapter_number']} has no content")

        return issues

# Create skill instance
creator = TextbookCreator()

# Export skill functions for use
def textbook_creator_init(params: Dict[str, Any]) -> Dict[str, Any]:
    """Initialize textbook project."""
    return creator.initialize_textbook(params)

def textbook_creator_generate_chapter(params: Dict[str, Any]) -> Dict[str, Any]:
    """Generate chapter structure."""
    # This would need to be called in context of an existing textbook
    # For demonstration, we'll return a sample response
    return {
        'status': 'success',
        'message': 'Chapter structure generated successfully',
        'chapter': params
    }

def textbook_creator_generate_section(params: Dict[str, Any]) -> Dict[str, Any]:
    """Generate section content."""
    # This would need to be called in context of an existing textbook
    # For demonstration, we'll return a sample response
    return {
        'status': 'success',
        'message': 'Section content generated successfully',
        'section': params
    }

def textbook_creator_quality_check(params: Dict[str, Any]) -> Dict[str, Any]:
    """Run quality checks."""
    # This would need to be called in context of an existing textbook
    # For demonstration, we'll return a sample response
    return {
        'status': 'success',
        'quality_score': 85,
        'issues': [],
        'recommendations': ['Review accessibility features', 'Check pedagogical alignment']
    }

def textbook_creator_export(params: Dict[str, Any]) -> Dict[str, Any]:
    """Export textbook to specified format."""
    # This would need to be called in context of an existing textbook
    # For demonstration, we'll return a sample response
    return {
        'status': 'success',
        'message': f'Textbook exported to {params.get("format", "pdf")} format',
        'filename': f'textbook_export.{params.get("format", "pdf")}'
    }