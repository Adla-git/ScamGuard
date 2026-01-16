import streamlit as st
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pipeline.scamdetector.detector import ScamDetector
from utils import get_logger

logger = get_logger(__name__)

def main():
    st.title("🛡️ ScamGuard AI")
    st.subheader("Detect Scam Messages with AI")
    
    # Initialize detector
    if 'detector' not in st.session_state:
        st.session_state.detector = ScamDetector()
        logger.info("ScamDetector initialized in Streamlit session")
    
    # Input section
    st.markdown("### Enter a message to analyze:")
    user_message = st.text_area(
        "Message to analyze:",
        placeholder="Enter the suspicious message here...",
        height=150
    )
    
    # Analysis button
    if st.button("🔍 Analyze Message", type="primary"):
        if user_message.strip():
            with st.spinner("Analyzing message..."):
                try:
                    result = st.session_state.detector.detect(user_message)
                    
                    # Display results
                    st.markdown("### Analysis Results")
                    
                    # Label with color coding
                    label = result.get('label', 'Unknown')
                    if label == 'Scam':
                        st.error(f"🚨 **Classification:** {label}")
                    elif label == 'Not Scam':
                        st.success(f"✅ **Classification:** {label}")
                    else:
                        st.warning(f"⚠️ **Classification:** {label}")
                    
                    # Reasoning
                    st.markdown("**Reasoning:**")
                    st.write(result.get('reasoning', 'No reasoning provided'))
                    
                    # Intent
                    st.markdown("**Detected Intent:**")
                    st.write(result.get('intent', 'Unknown intent'))
                    
                    # Risk factors
                    risk_factors = result.get('risk_factors', [])
                    if risk_factors:
                        st.markdown("**Risk Factors:**")
                        for factor in risk_factors:
                            st.write(f"• {factor}")
                    
                    logger.info(f"Analysis completed for message with result: {label}")
                    
                except Exception as e:
                    st.error(f"Error during analysis: {str(e)}")
                    logger.error(f"Streamlit analysis error: {e}")
        else:
            st.warning("Please enter a message to analyze.")
    
    # Example messages
    st.markdown("### Example Messages to Test")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📧 Phishing Example"):
            st.session_state.example_message = "URGENT: Your bank account will be closed in 24 hours. Click this link to verify your identity: http://fake-bank.com/verify"
    
    with col2:
        if st.button("💰 Prize Scam Example"):
            st.session_state.example_message = "Congratulations! You've won $10,000! Call 1-800-SCAM-NOW to claim your prize immediately!"
    
    # Display example message if selected
    if 'example_message' in st.session_state:
        st.text_area("Selected Example:", value=st.session_state.example_message, height=100, key="example_display")
        if st.button("Use This Example"):
            st.rerun()

if __name__ == "__main__":
    main()