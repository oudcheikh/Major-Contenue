from __future__ import annotations

import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(prefix="/studio", tags=["Studio Cahier"])

PROJECT_ROOT = Path(__file__).resolve().parents[2]


class CahierFile(BaseModel):
    id: str
    title: str
    section: str
    lang: str
    html_path: str
    pdf_path: str


class CahierContent(BaseModel):
    cahier: CahierFile
    content: str
    updated_at: str | None
    size_bytes: int
    pdf_exists: bool


class SaveCahierRequest(BaseModel):
    content: str
    backup: bool = True


class ExportPdfResponse(BaseModel):
    pdf_path: str
    size_bytes: int
    generated_at: str


CAHIERS: dict[str, CahierFile] = {
    "francais-complet": CahierFile(
        id="francais-complet",
        title="Cahier francais complet",
        section="Francais, maths, sciences",
        lang="fr",
        html_path="6AF-MATH-SCIENCE-FRANCAIS/cahier_major_concours_final.html",
        pdf_path="6AF-MATH-SCIENCE-FRANCAIS/cahier_major_concours_final.pdf",
    ),
    "francais-version-papier": CahierFile(
        id="francais-version-papier",
        title="Cahier francais version papier",
        section="Francais, maths, sciences",
        lang="fr",
        html_path="6AF-MATH-SCIENCE-FRANCAIS/Cahier-Major-6AF-PREPA-CONCOURS-Version-Papier.html",
        pdf_path="cahier-francais.pdf",
    ),
    "arabe-complet": CahierFile(
        id="arabe-complet",
        title="Cahier arabe complet",
        section="Arabe, islamique, histoire-geographie",
        lang="ar",
        html_path="6AF-ARABE/Cahier-Major-Arabe-6AF.html",
        pdf_path="6AF-ARABE/Cahier-Major-Arabe-6AF.pdf",
    ),
    "arabe-langue-islamique": CahierFile(
        id="arabe-langue-islamique",
        title="Cahier langue arabe et islamique",
        section="Arabe, islamique",
        lang="ar",
        html_path="6AF-ARABE/Cahier-Major-LangueArabe-Islamique-6AF.html",
        pdf_path="6AF-ARABE/Cahier-Major-LangueArabe-Islamique-6AF.pdf",
    ),
    "arabe-histoire-geo": CahierFile(
        id="arabe-histoire-geo",
        title="Cahier histoire-geographie et civique",
        section="Histoire-geographie, civique",
        lang="ar",
        html_path="6AF-ARABE/Cahier-Major-HistoireGeo-Civique-6AF.html",
        pdf_path="6AF-ARABE/Cahier-Major-HistoireGeo-Civique-6AF.pdf",
    ),
}


def _project_path(relative_path: str) -> Path:
    path = (PROJECT_ROOT / relative_path).resolve()
    try:
        path.relative_to(PROJECT_ROOT)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail="Path outside project is not allowed") from exc
    return path


def _get_cahier(cahier_id: str) -> CahierFile:
    cahier = CAHIERS.get(cahier_id)
    if not cahier:
        raise HTTPException(status_code=404, detail=f"Cahier '{cahier_id}' not found")
    return cahier


def _file_updated_at(path: Path) -> str | None:
    if not path.exists():
        return None
    return datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="seconds")


def _chrome_executable() -> str:
    candidates = [
        os.environ.get("TUTOR_CHROME_PATH"),
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        shutil.which("chrome"),
        shutil.which("chrome.exe"),
        shutil.which("msedge"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
    ]
    for candidate in candidates:
        if candidate and (Path(candidate).exists() or shutil.which(candidate)):
            return candidate
    raise HTTPException(
        status_code=500,
        detail="Chrome/Edge introuvable. Definis TUTOR_CHROME_PATH ou installe Chrome.",
    )


@router.get("/cahiers")
async def list_cahiers():
    result = []
    for cahier in CAHIERS.values():
        html_path = _project_path(cahier.html_path)
        pdf_path = _project_path(cahier.pdf_path)
        result.append(
            {
                **cahier.model_dump(),
                "exists": html_path.exists(),
                "pdf_exists": pdf_path.exists(),
                "updated_at": _file_updated_at(html_path),
                "size_bytes": html_path.stat().st_size if html_path.exists() else 0,
            }
        )
    return result


@router.get("/cahiers/{cahier_id}", response_model=CahierContent)
async def read_cahier(cahier_id: str):
    cahier = _get_cahier(cahier_id)
    html_path = _project_path(cahier.html_path)
    pdf_path = _project_path(cahier.pdf_path)
    if not html_path.exists():
        raise HTTPException(status_code=404, detail=f"HTML file not found: {cahier.html_path}")

    content = html_path.read_text(encoding="utf-8")
    return CahierContent(
        cahier=cahier,
        content=content,
        updated_at=_file_updated_at(html_path),
        size_bytes=html_path.stat().st_size,
        pdf_exists=pdf_path.exists(),
    )


@router.put("/cahiers/{cahier_id}", response_model=CahierContent)
async def save_cahier(cahier_id: str, payload: SaveCahierRequest):
    cahier = _get_cahier(cahier_id)
    html_path = _project_path(cahier.html_path)
    pdf_path = _project_path(cahier.pdf_path)
    if not html_path.exists():
        raise HTTPException(status_code=404, detail=f"HTML file not found: {cahier.html_path}")

    if payload.backup:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = html_path.with_name(f"{html_path.stem}_bak_{stamp}{html_path.suffix}")
        shutil.copy2(html_path, backup_path)

    html_path.write_text(payload.content, encoding="utf-8")
    return CahierContent(
        cahier=cahier,
        content=payload.content,
        updated_at=_file_updated_at(html_path),
        size_bytes=html_path.stat().st_size,
        pdf_exists=pdf_path.exists(),
    )


@router.post("/cahiers/{cahier_id}/export-pdf", response_model=ExportPdfResponse)
async def export_cahier_pdf(cahier_id: str):
    cahier = _get_cahier(cahier_id)
    html_path = _project_path(cahier.html_path)
    pdf_path = _project_path(cahier.pdf_path)
    if not html_path.exists():
        raise HTTPException(status_code=404, detail=f"HTML file not found: {cahier.html_path}")

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    chrome = _chrome_executable()
    command = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        str(html_path),
    ]

    result = subprocess.run(command, capture_output=True, text=True, timeout=120)
    if result.returncode != 0 or not pdf_path.exists():
        raise HTTPException(
            status_code=500,
            detail=(result.stderr or result.stdout or "PDF generation failed").strip(),
        )

    return ExportPdfResponse(
        pdf_path=str(pdf_path),
        size_bytes=pdf_path.stat().st_size,
        generated_at=datetime.now().isoformat(timespec="seconds"),
    )
