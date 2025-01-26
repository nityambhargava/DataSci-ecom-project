# File: scripts/feature_generator.py
import pandas as pd
import os

def load_and_merge_data():
    """
    Loading Customers, Transactions, and Products datasets and merging them into a single dataset.
    """
    file_paths = {
        "customers": "../data/Customers.csv",
        "transactions": "../data/Transactions.csv",
        "products": "../data/Products.csv",
    }

    # Ensuring all files exist
    for name, path in file_paths.items():
        if not os.path.exists(path):
            raise FileNotFoundError(f"{name} file not found at {path}")

    # Loading data
    customers = pd.read_csv(file_paths["customers"])
    transactions = pd.read_csv(file_paths["transactions"])
    products = pd.read_csv(file_paths["products"])

    # Merging data
    transactions_products = pd.merge(transactions, products, on="ProductID", how="left")
    final_dataset = pd.merge(transactions_products, customers, on="CustomerID", how="left")

    return final_dataset


def generate_customer_features():
    """
    Generate features for the lookalike model.
    """
    merged_data = load_and_merge_data()

    # Debugging print
    print("Merged data columns:", merged_data.columns)

    # Generating features
    customer_features = merged_data.groupby("CustomerID").agg({
        "TransactionID": "count",  # Total no. of transactions
        "TotalValue": "sum",       # Total amount spent
    }).rename(columns={
        "TransactionID": "TotalTransactions",
        "TotalValue": "TotalAmountSpent"
    })

    # Adding average transaction value
    customer_features["AvgTransactionValue"] = (
        customer_features["TotalAmountSpent"] / customer_features["TotalTransactions"]
    )

    return customer_features, merged_data


if __name__ == "__main__":
    # Debugging script entry point
    print("Script started.")
    try:
        customer_features, merged_data = generate_customer_features()
        print("Generated customer features:")
        print(customer_features.head())

        # Saving outputs for debugging
        merged_data.to_csv("../output/merged_data.csv", index=False)
        customer_features.to_csv("../output/customer_features.csv", index=True)

        print("Script completed successfully.")
    except Exception as e:
        print(f"Error: {e}")
