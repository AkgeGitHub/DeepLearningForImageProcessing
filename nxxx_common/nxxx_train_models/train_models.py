import pytest
import sys
sys.path.append(r"D:\Models\DeepLearningForImageProcessing\pytorch_classification\Test11_efficientnetV2")

from pytorch_classification.Test11_efficientnetV2 import train
from loguru import logger



def test_train_efficientnetv2():
    logger.info("===========正在开始训练 efficientnetv2 模型==========")
    train.nxxx_train()
    logger.info("=========== efficientnetv2 模型训练结束===========")

