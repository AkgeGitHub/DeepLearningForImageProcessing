# 公共配置
# 1. 数据集路径
data_path = r"D:\Models\DeepLearningForImageProcessing\data_set\flower_photos"

# efficientnetv2 模型配置
efficientnetv2 = {
    'num_classes': 5,
    'epochs': 10,
    'batch-size': 8,
    'lr': 0.01,
    'lrf': 0.01,
    'data-path': data_path,
    'weights': r"D:\Models\DeepLearningForImageProcessing\pytorch_classification\Test11_efficientnetV2\weights\pre_efficientnetv2-s.pth",
    'freeze-layers': True,
    'device': "cuda:0"
}
