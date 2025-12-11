from pathlib import Path
from sorawm.core import SoraWM
from sorawm.schemas import CleanerType

# 确保你有 resources/dog_vs_sam.mp4 这个视频文件，如果没有，换成你自己的视频路径
# input_video_path = Path("resources/dog_vs_sam.mp4")

input_video_path = Path("/workspace/my_inputs")
output_video_path = Path("outputs/sora_watermark_removed")

# 确保输出目录存在
Path("outputs").mkdir(exist_ok=True)

# 使用 LAMA 模式（速度快）
print("正在处理...")
sora_wm = SoraWM(cleaner_type=CleanerType.LAMA)
sora_wm.run(input_video_path, Path(f"{output_video_path}_lama.mp4"))
print("完成！")