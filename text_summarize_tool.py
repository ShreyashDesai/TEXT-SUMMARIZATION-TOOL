pip install -r requirements.txt
# text_summarize_tool.py
# Internship Task 1 — AI Based Text Summarize Tool
# Author: [Your Name]

from transformers import pipeline

def ai_text_summarizer(text, max_length=130, min_length=30):
    """
    Summarize lengthy text using an AI (Transformer) model.

    Args:
        text (str): Input paragraph or article.
        max_length (int): Maximum summary length.
        min_length (int): Minimum summary length.

    Returns:
        str: AI-generated summary.
    """
    print("⚙️ Loading AI summarization model...")
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


    print("🤖 Generating summary using AI...")
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']


if __name__ == "__main__":
    # Example input article
    article = """
    Artificial Intelligence (AI) has become one of the most transformative technologies of the modern era.
    From healthcare and education to finance and transportation, AI systems are being integrated into nearly
    every industry. Machine learning, a subset of AI, allows systems to learn and improve from experience
    without being explicitly programmed. Deep learning, an even more advanced technique, uses neural networks
    with many layers to analyze various factors of data. While AI offers immense opportunities for innovation,
    it also raises ethical concerns regarding privacy, employment, and bias. Governments and organizations
    worldwide are now exploring frameworks to ensure responsible AI development.
    """

    print("📰 Original Text:\n", article)
    print("\n🧩 AI Summary:\n", ai_text_summarizer(article))
