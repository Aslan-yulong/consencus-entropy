from consensus_entropy import calculate_consensus_entropy, calculate_ocr_difference, get_best_ocr_result

def main():
    print("测试1: 计算两个OCR结果的差异")
    str1 = "Hello World"
    str2 = "Hello Wrld"
    diff = calculate_ocr_difference(str1, str2)
    print(f"OCR结果1: {str1}")
    print(f"OCR结果2: {str2}")
    print(f"标准化编辑距离: {diff:.4f}")
    print()

    print("测试2: 计算多个OCR结果的共识熵")
    ocr_results = [
        "人工智能",
        "人工智障",
        "人工智能",
        "人工智惠"
    ]
    print("OCR结果:")
    for i, result in enumerate(ocr_results, 1):
        print(f"{i}. {result}")
    
    entropy_values = calculate_consensus_entropy(ocr_results, task_type="ocr")
    print("\n每个结果的熵值:")
    for i, entropy in enumerate(entropy_values, 1):
        print(f"{i}. {entropy:.4f}")
    print()

    print("测试3: 计算多个OCR结果并获取最佳结果")
    identical_strings = ["测试文本1", "测试文本2", "文本2"]
    best_result, best_entropy = get_best_ocr_result(identical_strings, task_type="ocr")
    print("所有OCR结果:")
    for i, result in enumerate(identical_strings, 1):
        print(f"{i}. {result}")
    print(f"\n最佳OCR结果: {best_result}")
    print(f"最佳结果的熵值: {best_entropy:.4f}")

if __name__ == "__main__":
    main() 