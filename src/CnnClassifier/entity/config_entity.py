from dataclasses import dataclass
from pathlib import Path

#custom return type of a funtion using entity 
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path