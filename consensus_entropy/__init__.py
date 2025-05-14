"""
Consensus Entropy - A library for calculating consensus entropy between multiple strings.
Currently focused on OCR task using Levenshtein distance.
"""

from .core import calculate_consensus_entropy, calculate_ocr_difference, get_best_ocr_result

__version__ = "0.1.0"
__all__ = ["calculate_consensus_entropy", "calculate_ocr_difference", "get_best_ocr_result"] 