from pathlib import Path
import os

ROOT: Path = Path(__file__).resolve().parent.parent

ROOT = Path(os.getenv("ONESTREAM_ROOT", ROOT))

class P:
    # ---- core dirs ----
    ROOT           = ROOT
    BACKEND        = ROOT / "backend"
    CONFIG         = ROOT / "config"
    DATA           = ROOT / "data"
    NOTEBOOKS      = ROOT / "notebook"
    
    # ---- data files ----
    DATA_PROCESSED          = DATA / "processed"
    CLEAN_ANIME_CSV        = DATA_PROCESSED / "clean_anime.csv"
    ANIME_DATASET_CSV      = DATA / "anime_dataset.csv"
    
    # ---- model artifacts ----
    ANIME_FEATURES_FILE    = DATA_PROCESSED / "anime_features.csv"
    
    # ---- backend entrypoints (optional, for convenience) ----
    BACKEND_MAIN_PY        = BACKEND / "main.py"
    BACKEND_META_PY        = BACKEND / "meta.py"
    BACKEND_RECOMMEND_PY   = BACKEND / "recommend.py"
    
    # ---- notebooks ----
    NB_CONTENT_BASED       = NOTEBOOKS / "content_based_recommendation.ipynb"
    NB_DATA_LOADING        = NOTEBOOKS / "data_loading_and_cleaning.ipynb"
    NB_FEATURE_CREATION    = NOTEBOOKS / "feature_file_creation.ipynb"
    
    