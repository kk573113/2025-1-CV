import torch
import sys
from pathlib import Path

# [1] 모델 가중치 경로 (수정된 부분)
src = r'C:\Users\chungbuk\kickgard\yolov5\runs\train\kickboard_yolov5s6\weights\best.pt'

# [2] 로드: 최신 API 대응 (경고 제거)
model = torch.load(src, map_location='cpu', weights_only=False)

# [3] 모델 저장 경로
dst = 'converted_model.pt'

# [4] 저장 (필요 시 torch.save(model.state_dict(), ...) 로도 가능)
torch.save(model, dst)

print(f"✅ 모델이 성공적으로 저장되었습니다: {dst}")
