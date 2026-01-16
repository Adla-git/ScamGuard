# imports
from typing import List, Dict, Any
from .executor import LLMExecutor
from .parser import OutputParser
from .builder import build_prompt
from utils import get_logger

# logger
logger = get_logger(__name__)

# scam detection class
class ScamDetector:
    """
    Docstring for ScamDetector
    """

    def __init__(self, strategy: str = "react") -> None:
        """
        Initialized the scam detection pipeline.
        """
        self.executor = LLMExecutor()
        self.parser = OutputParser()
        self.strategy = strategy
        logger.info(f"Initialized ScamDetector with strategy -> {self.strategy}")

    def detect(self, message: str) -> Dict[str, Any]:
        """
        Runs the main scam detection pipeline.
        """
        logger.info(f"Started detection for input message")
        try:
            prompt = build_prompt(message, self.strategy)
            raw_response = self.executor.execute(prompt)
            parsed_result = self.parser.parse_llm_output(raw_response)
            
            logger.info(f"Detection successful!")
            return parsed_result

        except Exception as e:
            logger.error(f"Detection pipeline failed: {e}")
            return {
                "label": "Error",
                "reasoning": f"Pipeline failed: {str(e)}",
                "intent": "Unknown",
                "risk_factors": ["System Error"]
            }
    
    def detect_batch(self, messages: List[str]) -> List[Dict[str, Any]]:
        """
        Process multiple messages in batch.
        """
        logger.info(f"Started batch detection for {len(messages)} messages")
        results = []
        
        for i, message in enumerate(messages):
            logger.info(f"Processing message {i+1}/{len(messages)}")
            result = self.detect(message)
            results.append(result)
        
        logger.info(f"Batch detection completed")
        return results