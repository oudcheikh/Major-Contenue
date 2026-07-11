import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def _load_courses() -> dict:
    with open(DATA_DIR / "courses.json", encoding="utf-8") as f:
        return json.load(f)


_courses_cache: dict | None = None


def get_courses() -> dict:
    global _courses_cache
    if _courses_cache is None:
        _courses_cache = _load_courses()
    return _courses_cache


def get_subjects() -> list[dict]:
    return get_courses().get("subjects", [])


def find_lesson(lesson_id: str) -> dict | None:
    for subject in get_subjects():
        for lesson in subject.get("lessons", []):
            if lesson["id"] == lesson_id:
                return {**lesson, "subjectId": subject["id"], "subjectLabel": subject["label"]}
    return None


def get_lessons_by_subject(subject_id: str) -> list[dict]:
    for subject in get_subjects():
        if subject["id"] == subject_id:
            return subject.get("lessons", [])
    return []


def build_lesson_context(lesson_id: str) -> str:
    """Build a compact text context for a lesson, ready to inject into an LLM prompt."""
    lesson = find_lesson(lesson_id)
    if not lesson:
        return ""

    parts = [
        f"Matiere: {lesson['subjectLabel']}",
        f"Lecon: {lesson['title']}",
        f"Resume: {lesson.get('summary', '')}",
    ]

    key_points = lesson.get("keyPoints", [])
    if key_points:
        parts.append("Points cles: " + " | ".join(key_points))

    rule = lesson.get("rule")
    if rule:
        parts.append(f"Regle: {rule}")

    tip = lesson.get("tip")
    if tip:
        parts.append(f"Astuce: {tip}")

    return "\n".join(parts)


def list_all_lesson_ids() -> list[str]:
    ids = []
    for subject in get_subjects():
        for lesson in subject.get("lessons", []):
            ids.append(lesson["id"])
    return ids
