#!/usr/bin/env python
import sys
import warnings

from my_mas.crew import MyMas

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        "Product_Category": "Noise-Canceling Headphones",
        "Target_Brands": ['Sony', 'Bose', 'Apple', 'Sennheiser', 'Beats'],
        "Needs_Features": "High-quality sound, long battery life, comfortable for extended wear, good noise cancellation, suitable for professional and personal use"
    }
    MyMas().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        MyMas().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MyMas().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'Product_Category': 'Noise-Canceling Headphones',
        'Target_Brands': ['Sony', 'Bose', 'Apple', 'Sennheiser', 'Beats', 'Bowers & Wilkins'],
        'Needs_Features': 'Superior audio quality, active noise cancellation, long battery life, comfortable design good for music and professional use'
    }
    try:
        MyMas().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()
