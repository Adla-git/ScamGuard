#!/usr/bin/env python3

from pipeline.scamdetector.detector import ScamDetector
import json

def test_strategies():
    """Test different prompt strategies"""
    
    test_message = "URGENT: Your account will be suspended! Click here immediately to verify: http://fake-bank.com"
    
    strategies = ["react", "simple", "detailed"]
    
    for strategy in strategies:
        print(f"\n=== Testing {strategy.upper()} Strategy ===")
        detector = ScamDetector(strategy=strategy)
        result = detector.detect(test_message)
        print(f"Label: {result['label']}")
        print(f"Reasoning: {result['reasoning'][:100]}...")

def test_batch_processing():
    """Test batch processing functionality"""
    
    print("\n=== Testing Batch Processing ===")
    
    messages = [
        "Congratulations! You've won $10,000! Call now!",
        "Your package delivery is scheduled for tomorrow at 2pm.",
        "URGENT: Verify your bank account or it will be closed!",
        "Meeting reminder: Team standup at 10am in conference room A."
    ]
    
    detector = ScamDetector(strategy="simple")
    results = detector.detect_batch(messages)
    
    for i, (msg, result) in enumerate(zip(messages, results)):
        print(f"\nMessage {i+1}: {msg[:50]}...")
        print(f"Result: {result['label']}")

if __name__ == "__main__":
    test_strategies()
    test_batch_processing()