from fastapi import APIRouter, HTTPException

from services.knowledge import get_courses, get_subjects, find_lesson, get_lessons_by_subject

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.get("/")
async def list_subjects():
    """List all subjects with their lesson count."""
    subjects = get_subjects()
    return [
        {
            "id": s["id"],
            "label": s["label"],
            "labelAr": s.get("labelAr", ""),
            "color": s.get("color"),
            "icon": s.get("icon"),
            "lesson_count": len(s.get("lessons", [])),
        }
        for s in subjects
    ]


@router.get("/all")
async def get_all_courses():
    """Return the full courses.json content."""
    return get_courses()


@router.get("/subject/{subject_id}")
async def get_subject_lessons(subject_id: str):
    """Get all lessons for a subject."""
    lessons = get_lessons_by_subject(subject_id)
    if not lessons:
        raise HTTPException(status_code=404, detail=f"Subject '{subject_id}' not found")
    return lessons


@router.get("/lesson/{lesson_id}")
async def get_lesson(lesson_id: str):
    """Get a single lesson by ID with full details."""
    lesson = find_lesson(lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail=f"Lesson '{lesson_id}' not found")
    return lesson
