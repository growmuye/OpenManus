import asyncio

from app.agent.lxy_manus_v1_1 import LxyManus_v1_1
from app.logger import logger


async def main():
    agent = LxyManus_v1_1()
    try:
        # 从文件中读取 prompt
        file_path = "doc/招聘JD.txt"  # 替换为你的文件路径
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                prompt = file.read().strip()
                if not prompt:
                    logger.warning("Empty prompt provided.")
                    return
        except Exception as e:
            logger.warning(f"Error reading file: {e}")
            return
        logger.warning("Processing your request...")
        logger.info(f"prompt:\n{prompt}")
        print(f"prompt:\n{prompt}")
        await agent.run(prompt)
        logger.info("Request processing completed.")
    except KeyboardInterrupt:
        logger.warning("Operation interrupted.")
    finally:
        # Ensure agent resources are cleaned up before exiting
        await agent.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
