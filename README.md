# Consensus Entropy | 共识熵

[English](#english) | [中文](#chinese)

<a name="english"></a>
## English

A Python library for calculating consensus entropy between multiple strings, particularly useful for OCR result analysis. Uses Levenshtein distance to calculate string differences.

### Citation

If you use this library in your research, please cite our paper:

```bibtex
@misc{zhang2025consensusentropyharnessingmultivlm,
      title={Consensus Entropy: Harnessing Multi-VLM Agreement for Self-Verifying and Self-Improving OCR}, 
      author={Yulong Zhang and Tianyi Liang and Xinyue Huang and Erfei Cui and Xu Guo and Pei Chu and Chenhui Li and Ru Zhang and Wenhai Wang and Gongshen Liu},
      year={2025},
      eprint={2504.11101},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2504.11101}
}
```

### Installation

```bash
pip install consensus-entropy
```

### Usage

#### Basic Usage

```python
from consensus_entropy import calculate_consensus_entropy

# Calculate consensus entropy for multiple OCR results
ocr_results = [
    "Hello World",
    "Hello Wrld",
    "Hallo World"
]

# Calculate entropy values for each result
entropy_values = calculate_consensus_entropy(ocr_results, task_type="ocr")
print(entropy_values)  # [0.1667, 0.3333, 0.3333]
```

#### Get Best OCR Result

```python
from consensus_entropy import get_best_ocr_result

# Get the OCR result with lowest entropy
ocr_results = ["Test1", "Test2", "Text2"]
best_result, best_entropy = get_best_ocr_result(ocr_results, task_type="ocr")
print(f"Best result: {best_result}")
print(f"Entropy: {best_entropy:.4f}")
```

### Features

- Calculate normalized Levenshtein distance
- Compute consensus entropy for multiple strings
- Get the best OCR result with lowest entropy
- Support for both English and Chinese text
- Type hints for better IDE support
- Optimized for OCR tasks

### Requirements

- Python 3.7+
- numpy
- python-Levenshtein

### Notes

- Currently only supports OCR task type
- Input string list must contain at least two elements
- All inputs will be converted to string type

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

<a name="chinese"></a>
## 中文

一个用于计算多个字符串之间共识熵的Python库，特别适用于OCR结果分析。使用Levenshtein距离来计算字符串之间的差异。

### 引用

如果您在研究中使用了本库，请引用我们的论文：

```bibtex
@misc{zhang2025consensusentropyharnessingmultivlm,
      title={Consensus Entropy: Harnessing Multi-VLM Agreement for Self-Verifying and Self-Improving OCR}, 
      author={Yulong Zhang and Tianyi Liang and Xinyue Huang and Erfei Cui and Xu Guo and Pei Chu and Chenhui Li and Ru Zhang and Wenhai Wang and Gongshen Liu},
      year={2025},
      eprint={2504.11101},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2504.11101}
}
```

### 安装

```bash
pip install consensus-entropy
```

### 使用方法

#### 基本用法

```python
from consensus_entropy import calculate_consensus_entropy

# 计算多个OCR结果的共识熵
ocr_results = [
    "人工智能",
    "人工智障",
    "人工智能",
    "人工智惠"
]

# 计算每个结果的熵值
entropy_values = calculate_consensus_entropy(ocr_results, task_type="ocr")
print(entropy_values)  # [0.1667, 0.2500, 0.1667, 0.2500]
```

#### 获取最佳OCR结果

```python
from consensus_entropy import get_best_ocr_result

# 获取熵值最低的OCR结果
ocr_results = ["测试文本1", "测试文本2", "文本2"]
best_result, best_entropy = get_best_ocr_result(ocr_results, task_type="ocr")
print(f"最佳结果: {best_result}")
print(f"熵值: {best_entropy:.4f}")
```

### 功能特点

- 计算标准化Levenshtein距离
- 计算多个OCR结果的共识熵
- 获取熵值最低的最佳OCR结果
- 支持中文和英文文本
- 类型提示支持
- 针对OCR任务优化的算法

### 系统要求

- Python 3.7+
- numpy
- python-Levenshtein

### 注意事项

- 目前仅支持OCR任务类型
- 输入字符串列表至少需要两个元素
- 所有输入都会被转换为字符串类型处理

### 许可证

本项目采用MIT许可证 - 详见LICENSE文件

### 贡献

欢迎提交Pull Request来改进这个项目。 