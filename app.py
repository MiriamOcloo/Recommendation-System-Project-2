import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Recommender", page_icon="", layout="wide")

st.title("Recommendation System")
st.markdown("Get intelligent product recommendations based on user browsing behavior")

# Load your trained model
try:
    with open('category_recommender.pkl', 'rb') as f:
        recommender = pickle.load(f)
    st.sidebar.success("Model loaded successfully!")
except Exception as e:
    st.sidebar.error(f"Model loading failed: {str(e)}")

# Load your association rules for display
try:
    rules_df = pd.read_csv('association_rules_recommendations.csv')
    st.sidebar.info(f" {len(rules_df)} association rules loaded")
except:
    st.sidebar.warning(" Rules file not found")

# User input section
st.sidebar.header(" Input Parameters")
viewed_categories = st.sidebar.text_input("Categories Viewed (comma-separated)", "1483, 959")
top_n = st.sidebar.slider("Number of Recommendations", 1, 10, 3)

# Recommendation function
if st.button(" Get Recommendations", type="primary"):
    try:
        categories = [float(x.strip()) for x in viewed_categories.split(",") if x.strip()]
        if categories:
            recommendations = recommender.recommend(categories, top_n)
            
            st.success(f" Generated {len(recommendations)} recommendations!")
            
            # Display recommendations
            for i, (cat_id, confidence) in enumerate(recommendations, 1):
                st.info(f"**#{i}: Category {cat_id}** - {confidence:.1%} confidence")
        else:
            st.warning(" Please enter valid category numbers")
            
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Show system stats
st.sidebar.markdown("---")
st.sidebar.markdown("** System Performance**")
st.sidebar.write("• 409 association rules discovered")
st.sidebar.write("• 73.9% max prediction accuracy")
st.sidebar.write("• 6.91x better than random")
st.sidebar.write("• 17x lift on best patterns")

# Add some examples
st.sidebar.markdown("---")
st.sidebar.markdown("** Try These Examples:**")
st.sidebar.write("• `1483, 959` → Predicts Category 1051")
st.sidebar.write("• `57, 1483` → Predicts Category 959")
st.sidebar.write("• `1384, 1135` → Predicts Category 589")
