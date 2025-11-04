from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class CodeMetrics:
    """Контейнер для метрик одного файла."""
    file_path: str
    cyclomatic_complexity: int
    lines_of_code: int
    number_of_functions: int
    number_of_classes: int


class MetricsAnalyzer:
    def init(self, ast_tree: ast.AST, file_path: str):
        self.tree = ast_tree
        self.file_path = file_path

    def calculate_all(self) -> Dict[str, Any]:
