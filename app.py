import streamlit as st
import pandas as pd
import ast

class CategoryRecommender:
    def __init__(self, rules_df):
        self.rules = rules_df.copy()
        self.rule_map = {}
        for _, rule in self.rules.iterrows():
            # Convert string representation to actual Python sets/lists
            try:
                if isinstance(rule['antecedents'], str):
                    antecedents = frozenset(ast.literal_eval(rule['antecedents']))
                else:
                    antecedents = frozenset(rule['antecedents'])
                
                if isinstance(rule['consequents'], str):
                    consequent = list(ast.literal_eval(rule['consequents']))[0]
                else:
                    consequent = list(rule['consequents'])[0]
                
                if antecedents not in self.rule_map:
                    self.rule_map[antecedents] = []
                self.rule_map[antecedents].append((consequent, rule['confidence']))
            except:
                continue
    
    def recommend(self, viewed_categories, top_n=3):
        viewed_set = set(viewed_categories)
        recommendations = {}
        
        for antecedents, conseqs in self.rule_map.items():
            if antecedents.issubset(viewed_set):
                for consequent, confidence in conseqs:
                    if consequent not in viewed_set:
                        if consequent not in recommendations or confidence > recommendations[consequent]:
                            recommendations[consequent] = confidence
        
        sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
        return sorted_recommendations[:top_n]

# Initialize the app
st.set_page_config(page_title="E-Commerce Recommender", page_icon="", layout="wide")
st.title(" E-Commerce Recommendation System")

# Load rules from CSV (more reliable than pickle)
try:
    rules_df = pd.read_csv('association_rules_recommendations.csv')
    recommender = CategoryRecommender(rules_df)
    st.sidebar.success(f" Loaded {len(rules_df)} association rules!")
except Exception as e:
    st.sidebar.error(f" Failed to load rules: {str(e)}")
    recommender = None

# User interface
if recommender:
    viewed_categories = st.sidebar.text_input("Categories Viewed (comma-separated)", "1483, 959")
    top_n = st.sidebar.slider("Number of Recommendations", 1, 10, 3)
    
    if st.button("Get Recommendations"):
        try:
            categories = [float(x.strip()) for x in viewed_categories.split(",") if x.strip()]
            recommendations = recommender.recommend(categories, top_n)
            
            st.success(f"Generated {len(recommendations)} recommendations!")
            for i, (cat_id, confidence) in enumerate(recommendations, 1):
                st.info(f"**#{i}: Category {cat_id}** - {confidence:.1%} confidence")
                
        except Exception as e:
            st.error(f"Error: {str(e)}")
else:
    st.error("Could not initialize the recommendation system. Please check your data files.")
