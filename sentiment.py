import pandas as pd
from nltk import download
from nltk.sentiment import SentimentIntensityAnalyzer
import os


# Download the VADER lexicon required for SentimentIntensityAnalyzer
download('vader_lexicon')

# Initialize VADER
sia = SentimentIntensityAnalyzer()

# Define folder paths
input_folder = "DataMiningProcessing"  
output_folder = "Processed"

# if output folder doesn't exist, create one
os.makedirs(output_folder, exist_ok=True)

def process_csv(file_path, output_path):

    # Load the file path
    pf  = pd.read_csv(file_path)

    # sia.polarity_scores creates a dictorary for the values pos, neg, neu, and compound 
    #   ex: {'neg': 0.0, 'neu': 0.182, 'pos': 0.818, 'compound': 0.6696}

    # Saving and Labeling the Compound Value
    # Apply Setiment Score to each string of CSV Column
    pf['Sentiment_Score'] = pf['content'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
    pf['Sentiment_Label'] = pf['Sentiment_Score'].apply(
        lambda score: 'Positive' if score > 0.05 else 'Negative' if score < -0.05 else 'Neutral'
    )

    # Save the new csv file with their scores
    pf.to_csv(output_path, index=False)
    print(f"Processed and saved: {output_path}")

# Perform sia.process_csv on all CSV files in the DataMiningProcess folder
for file_name in os.listdir(input_folder):
    if file_name.endswith('.csv'):  # Check if the file is a CSV
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        # get rid of the 'bluesky_posts_' to get only the sports name
        # later to load into the result 
        output_file_name = file_name.replace("bluesky_posts_", "")
        output_path = os.path.join(output_folder, output_file_name)

        print(f"Processing file: {file_name}")
        process_csv(input_path, output_path)

import pandas as pd
import os

#Store the Results
results = []
processed_folder = "Processed"

# Define the output folder, one directory before 'Processed'
output_folder = os.path.abspath(os.path.join(processed_folder, ".."))
output_file = os.path.join(output_folder, "sports_sentiment_matrix.xlsx") 

# Loop through the processed folder and calculate the mean sentiment scores for each sport
for file_name in os.listdir(processed_folder):
    if file_name.endswith('.csv'):
        file_path = os.path.join(processed_folder, file_name)
        pf = pd.read_csv(file_path)
        
        # Calculate the average  score on sentiment column
        avg_sentiment_score = pf['Sentiment_Score'].mean()
        
        # Determine the sentiment score for the avergage score
        avg_sentiment_label = "Positive" if avg_sentiment_score > 0.05 else "Negative" if avg_sentiment_score < -0.05 else "Neutral"
        
        # remove .csv
        sport_name = file_name.replace(".csv", "")
        
        # Append the data to the list
        results.append({
            'Sport': sport_name,
            'Average Sentiment Score': avg_sentiment_score,
            'Sentiment Label': avg_sentiment_label
        })

# connect to output_folder
os.makedirs(output_folder, exist_ok=True)


# Convert the list of data into a pandas DataFrame
# Save the DataFrame to an Excel file in the parent folder
sentiment_pf = pd.DataFrame(results)
sentiment_pf.to_excel(output_file, index=False, engine='openpyxl')

print(f"Sentiment analysis results saved to {output_file}")