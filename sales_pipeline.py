import os
import pandas as pd
import matplotlib.pyplot as plt
            

def load_csv(fpath:str) -> pd.DataFrame:
    """Loads the dataset and returns it"""
    try:
        return pd.read_csv(fpath)
    except FileNotFoundError:
        raise FileNotFoundError("Dataset Sales_April_2019.csv was not found.")

def convert_sales_data_type(df:pd.DataFrame) -> pd.DataFrame:
    """Converts columns to appropriate data types"""
    df = df.copy()
    df["Quantity Ordered"] = pd.to_numeric(df["Quantity Ordered"],errors="coerce")
    df["Price Each"] = pd.to_numeric(df["Price Each"],errors="coerce")
    df["Order Date"] = pd.to_datetime(df["Order Date"],format="%m/%d/%y %H:%M",errors="coerce")
    return df
 

def clean_data(df:pd.DataFrame) -> pd.DataFrame:
    """Cleans the data for further analysis"""
    df = df.copy()
    df = df.dropna(how='all')
    df = convert_sales_data_type(df)
    df = df[df.ne(df.columns).all(axis=1)]
    df = df.dropna()
    return df


def enrich_data(df:pd.DataFrame) -> pd.DataFrame:
    """Enriches the dataset with the following columns : Revenue, Month, Hour and City"""
    df = df.copy()
    df["Revenue"] = df["Quantity Ordered"] * df["Price Each"]
    df["Hour"] = df["Order Date"].dt.hour
    df["City"] = df["Purchase Address"].apply(lambda x: x.split(',')[1].strip())
    df["Month"] = df["Order Date"].dt.month
    return df

def compute_kpis(df:pd.DataFrame) -> dict :
    """Returns the following dictionary with the keys :
    revenue_total >> float which contains the gross revenue
    revenue_by_city >> DataFrame which contains the gross revenue made by city
    revenue_by_hour >> DataFrame which contains the gross revenue made per hour
    revenue_by_month >> DataFrame which contains the gross revenue made per month
    revenue_by_product >> DataFrame which contains the gross revenue made by product
    product_sold_by_hour >> DataFrame which contains the quantity of product sold per hour
    top_product >> DataFrame which contains the total quantity of product sold by product
    best_revenue_hour >> int which contains the hour during which the most sales occurred
    best_revenue_month >> int which contains the month during which the most sales occurred
    best_revenue_city >> str which contains the city which generated the highest revenue
    best_product_by_quantity >> str which contains the product with the highest quantity sold
    orders_by_city >> DataFrame which contains the number of orders made in a city
    orders_by_hour >> DataFrame which contains the number of orders made every hour
    average_order_value >> float which contains the average revenue made per order
    best_revenue_product >> str which contains the name of the product that made the best revenue
    city_with_most_orders >> str which contains the name of the city with the most orders
    hour_with_most_orders >> int which contains the hour with the most orders
    average_revenue_by_order_by_city >> DataFrame which contains the average revenue per order by city
    orders_per_product >> DataFrame which contains the number of orders per product
    top_5_products >> DataFrame which contains the 5 most sold products
    top_5_cities >> DataFrame which contains the 5 cities with the highest revenue
    """
    #Revenue KPIs
    revenue_total = df["Revenue"].sum()
    revenue_by_city = df.groupby("City")["Revenue"].sum().sort_values(ascending=False).to_frame()
    revenue_by_hour = df.groupby("Hour")["Revenue"].sum().to_frame()
    revenue_by_month = df.groupby("Month")["Revenue"].sum().to_frame()
    revenue_by_product = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).to_frame()
    best_revenue_hour = revenue_by_hour["Revenue"].idxmax()
    best_revenue_month = revenue_by_month["Revenue"].idxmax()
    best_revenue_city = revenue_by_city["Revenue"].index[0]
    best_revenue_product = revenue_by_product.index[0]
    top_5_cities = revenue_by_city.head(5)
    average_revenue_by_order_by_city = df.groupby("City")["Revenue"].mean().sort_values(ascending=False).to_frame()
    
    #Product KPIs
    top_product = df.groupby("Product")["Quantity Ordered"].sum().sort_values(ascending=False).to_frame()
    product_sold_by_hour = df.groupby("Hour")["Quantity Ordered"].sum().to_frame()
    best_product_by_quantity = top_product.index[0]
    top_5_products = top_product.head(5)
    
    #Order KPIs
    orders_by_city = df.groupby("City")["Order ID"].nunique().sort_values(ascending=False).to_frame()
    orders_by_hour = df.groupby("Hour")["Order ID"].nunique().to_frame()
    average_order_value = df.groupby("Order ID")["Revenue"].sum().mean()
    city_with_most_orders = orders_by_city.index[0]
    hour_with_most_orders = orders_by_hour.idxmax()
    orders_per_product = df.groupby("Product")["Order ID"].nunique().sort_values(ascending=False).to_frame()
   
    return {
    "revenue_total" : revenue_total,
    "revenue_by_city" : revenue_by_city,
    "revenue_by_hour" : revenue_by_hour,
    "revenue_by_month" : revenue_by_month,
    "revenue_by_product" : revenue_by_product,
    "product_sold_by_hour" : product_sold_by_hour,
    "top_product" : top_product,
    "best_revenue_hour" : best_revenue_hour,
    "best_revenue_month" : best_revenue_month,
    "best_revenue_city" : best_revenue_city,
    "best_product_by_quantity" : best_product_by_quantity,
    "orders_by_city" : orders_by_city,
    "orders_by_hour" : orders_by_hour,
    "average_order_value" : average_order_value,
    "best_revenue_product" : best_revenue_product,
    "city_with_most_orders" : city_with_most_orders,
    "hour_with_most_orders" : hour_with_most_orders,
    "average_revenue_by_order_by_city" : average_revenue_by_order_by_city,
    "orders_per_product" : orders_per_product,
    "top_5_products" : top_5_products,
    "top_5_cities" : top_5_cities
    }

    
def export_results(kpis:dict,df:pd.DataFrame=None) -> None:
    """Exports KPIs and optional DataFrame to CSV files"""
    os.makedirs("output", exist_ok=True)
    for data in kpis.keys():
        if not isinstance(kpis.get(data), pd.DataFrame):
            continue
        kpis[data].to_csv('output/' +data+'.csv', index=False)
    if df is not None:
        df.to_csv('output/enriched_April_Sales_2019.csv', index=False)
    
def save_plot(df:pd.DataFrame, kind:str, title:str, ylabel:str, filename:str) -> None:
    df.plot(ylabel=ylabel,title=title,kind=kind,figsize=(13, 8))
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.25)
    plt.tight_layout()
    if kind == "line":
        plt.grid()
    plt.savefig("plots/"+filename+".png")
    plt.close() 

def create_plots(kpis:dict) -> None:
    """Exports kpis as graphs in PNG"""
    os.makedirs("plots", exist_ok=True)

    # Revenue plots
    save_plot(kpis["revenue_by_city"], ylabel="Revenue", title="Revenue by City", kind="bar", filename="revenue_by_city")
    save_plot(kpis["revenue_by_hour"], ylabel="Revenue", title="Revenue by Hour", kind="bar", filename="revenue_by_hour")
    save_plot(kpis["revenue_by_month"], ylabel="Revenue", title="Revenue by Month", kind="bar", filename="revenue_by_month")
    save_plot(kpis["revenue_by_product"], ylabel="Revenue", title="Revenue by Product", kind="bar", filename="revenue_by_product")
    save_plot(kpis["average_revenue_by_order_by_city"], ylabel="Average Revenue per orders", title="Average Revenue by Orders per City", kind="bar", filename="average_revenue_by_order_by_city")
    save_plot(kpis["top_5_cities"], ylabel="Revenue", title="Top 5 Cities by Revenue", kind="bar", filename="top_5_cities")

    # Product plots
    save_plot(kpis["product_sold_by_hour"], ylabel="Quantity", title="Products Sold by Hour", kind="line", filename="product_sold_by_hour")
    save_plot(kpis["top_product"], ylabel="Quantity", title="Quantity of Products Sold", kind="bar", filename="top_product")
    save_plot(kpis["top_5_products"], ylabel="Quantity", title="Top 5 Products by Quantity Sold", kind="bar", filename="top_5_products")
    save_plot(kpis["orders_per_product"], ylabel="Orders", title="Orders per Product", kind="bar", filename="orders_per_product")

    # Order plots
    save_plot(kpis["orders_by_city"], ylabel="Orders", title="Orders by City", kind="bar", filename="orders_by_city")
    save_plot(kpis["orders_by_hour"], ylabel="Orders", title="Orders by Hour", kind="bar", filename="orders_by_hour")


def main():
    data = load_csv("data/Sales_April_2019.csv")
    data = clean_data(data)
    print(data.head(10))
    data.info()
    data = enrich_data(data)
    kpis = compute_kpis(data)
    export_results(kpis)
    create_plots(kpis)

if __name__ == "__main__":
    main()
