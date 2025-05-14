"""
Core functionality for calculating consensus entropy.
"""

from typing import List, Union, Literal, Tuple
from Levenshtein import distance as Levenshtein_distance
import numpy as np

def calculate_ocr_difference(a: str, b: str) -> float:
    """
    Calculate the normalized Levenshtein distance between two strings for OCR results.
    
    Args:
        a (str): First string
        b (str): Second string
        
    Returns:
        float: Normalized Levenshtein distance between the strings
    """
    a_str = str(a)
    b_str = str(b)
    max_len = max(len(a_str), len(b_str))
    if max_len == 0:
        return 0.0
    return Levenshtein_distance(a_str, b_str) / max_len

def calculate_consensus_entropy(
    strings: List[str],
    task_type: Literal["ocr"] = "ocr"
) -> List[float]:
    """
    Calculate consensus entropy for a list of strings.
    Currently only supports OCR task using Levenshtein distance.
    
    Args:
        strings (List[str]): List of strings to calculate consensus entropy for
        task_type (Literal["ocr"]): Type of task. Currently only supports "ocr"
        
    Returns:
        List[float]: List of entropy values for each string
        
    Raises:
        ValueError: If the input list is empty or contains only one string
        ValueError: If task_type is not supported
    """
    if not strings:
        raise ValueError("Input list cannot be empty")
    if len(strings) == 1:
        raise ValueError("At least two strings are required to calculate consensus entropy")
    
    if task_type != "ocr":
        raise ValueError("Currently only 'ocr' task type is supported")
    
    n = len(strings)
    entropy_values = []
    
    for i in range(n):
        differences = []
        for j in range(n):
            if i != j:
                diff = calculate_ocr_difference(strings[i], strings[j])
                differences.append(diff)
        entropy_values.append(np.mean(differences))
    
    return entropy_values

def get_best_ocr_result(
    strings: List[str],
    task_type: Literal["ocr"] = "ocr"
) -> Tuple[str, float]:
    """
    Get the OCR result with the lowest entropy value.
    
    Args:
        strings (List[str]): List of OCR results
        task_type (Literal["ocr"]): Type of task. Currently only supports "ocr"
        
    Returns:
        Tuple[str, float]: The best OCR result and its entropy value
        
    Raises:
        ValueError: If the input list is empty or contains only one string
        ValueError: If task_type is not supported
    """
    entropy_values = calculate_consensus_entropy(strings, task_type)
    best_idx = np.argmin(entropy_values)
    return strings[best_idx], entropy_values[best_idx] 