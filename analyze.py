import pandas as pd
import matplotlib.pyplot as pp
import seaborn as sns
import datetime
from datetime import datetime

df = pd.read_csv("Superstore Management System.csv")
print(df)

print(df.head())
print(df.tail())
print(df.dtypes)
print(df.sample())
print(df.info())
print(df.columns)
print(df.shape)
print(df.describe(include = 'object'))
print("data Quality")
print("Missing values : ")
missing_data = df.isnull().sum()
print(missing_data[missing_data>0])

print(f"\nduplicate rows : {df.duplicated().sum()}")

df['order date'] = pd.to_datetime(df['order date'] , format = '%Y-%m-%d')
df['ship date'] = pd.to_datetime(df['ship date'] , format = '%Y-%m-%d')

print("\nDate columns converted :\n")
print(f"order date : {df['order date'].dtype}")
print(f"ship date : {df['ship date'].dtype}")

#univariate analysis
print("...categorical variables...")
categorial_cols = ['category', 'Payment Mode', 'Delivery status', 'Auto reorder']


for col in categorial_cols :
    print(f"\n...{col}...")
    print(df[col].value_counts())

    #visualization
    pp.figure(figsize =(5,5))
    df[col].value_counts().plot(kind = 'bar' , color = 'skyblue')
    pp.title(f"distribution of {col}")
    pp.xticks(rotation = 30)
    pp.tight_layout()
    pp.savefig(f"{col}_distribution.png")
    pp.close()

#numerical variable analysis
print("...numerical variables...")
num_cols = ['Quantity' , 'Unit price' , 'discount(%)' , 'Sales amount' , 'cost price' , 'profit' , 'stock left' , 'reorder quantity']

for col in num_cols :
    print(f"\n...{col}...\n")
    print(f"Mean : {df[col].mean():.2f}")
    print(f"Median : {df[col].median():.2f}")
    print(f"std dev : {df[col].std():.2f}")
    print(f"Min : {df[col].min():.2f}")
    print(f"Max : {df[col].max():.2f}")

    pp.figure(figsize = (5,3))
    pp.subplot(1,2,1)
    df[col].hist(bins = 30 , color = 'green' , alpha = 0.5)
    pp.title(f"distribution of {col}")
    pp.tight_layout()
    pp.savefig(f"{col}_histogram.png")
    pp.close()

#bivariate analysis
print("..sales and profit by category..")

cat_performance = df.groupby('category').agg({
    'Sales amount' : 'sum',
    'profit' : 'sum',
    'Order id' : 'count'
}).rename(columns = {'Order id' : 'Order count'})

cat_performance['profit margin'] = (cat_performance['profit']/cat_performance['Sales amount'])* 100
print(cat_performance , '\n\n')

#visualization
fig, axes = pp.subplots(2,2,figsize = (15,12))

#sales by category
cat_performance['Sales amount'].plot(kind = 'bar' , ax = axes[0,0] , color = 'blue' , alpha = 0.5)
axes[0,0].set_title("Total sales by category")
axes[0,0].tick_params(axis = 'x' , rotation = 30)

#profit by category
cat_performance['profit'].plot(kind = 'bar' , ax = axes[0,1] , color = 'green' , alpha = 0.5)
axes[0,1].set_title("Total profit by category")
axes[0,1].tick_params(axis = 'x' , rotation = 30)

#order count by category
cat_performance['Order count'].plot(kind = 'bar' , ax = axes[1,0] , color = 'red' , alpha = 0.5)
axes[1,0].set_title("Order count by category")
axes[1,0].tick_params(axis = 'x' , rotation = 30)

#profit margin by category
cat_performance['profit margin'].plot(kind = 'bar' , ax = axes[1,1] , color = 'orange' , alpha = 0.5)
axes[1,1].set_title("Profit margin by category")
axes[1,1].tick_params(axis = 'x' , rotation = 30)

pp.tight_layout()
pp.savefig('category_performance.png')
pp.close()

#regional performance
print("...regional performance...")

reg_performance = df.groupby('region').agg({
    'Sales amount' : 'sum',
    'profit' : 'sum' ,
    'Order id' : 'count'
}).rename(columns= {'Order id' : 'Order count'})

reg_performance['profit margin'] = (reg_performance['profit']/reg_performance['Sales amount']) * 100
print(reg_performance , '\n\n')

#visualization
fig, axes = pp.subplots(2,2,figsize = (15,12))

#sales by region
reg_performance['Sales amount'].plot(kind = 'bar' , ax = axes[0,0] , color = 'blue' , alpha = 0.5)
axes[0,0].set_title("Total sales by region")
axes[0,0].tick_params(axis = 'x' , rotation = 30)

#profit by region
reg_performance['profit'].plot(kind = 'bar' , ax = axes[0,1] , color = 'green' , alpha = 0.5)
axes[0,1].set_title("Total profit by region")
axes[0,1].tick_params(axis = 'x' , rotation = 30)

#order count by region
reg_performance['Order count'].plot(kind = 'bar' , ax = axes[1,0] , color = 'red' , alpha = 0.5)
axes[1,0].set_title("Order count by region")
axes[1,0].tick_params(axis = 'x' , rotation = 30)

#profit margin by region
reg_performance['profit margin'].plot(kind = 'bar' , ax = axes[1,1] , color = 'orange' , alpha = 0.5)
axes[1,1].set_title("Profit margin by region")
axes[1,1].tick_params(axis = 'x' , rotation = 30)

pp.tight_layout()
pp.savefig('regional_performance.png')
pp.close()

#Time series analysis
print("..Time Series Analysis...")

df['Order Month'] = df['order date'].dt.to_period('M')
df['Order Year'] = df['order date'].dt.year

#monthly trends
monthly_trends = df.groupby('Order Month').agg({
    "Sales amount" : 'sum',
    'profit' : 'sum' ,
    'Order id' : 'count'
}).rename(columns = {'Order id' : 'Order count'})

print('Monthly trends : ')
print(monthly_trends.tail(10), '\n\n')

#visualization
pp.figure(figsize = (15,10))

pp.subplot(3,1,1)
monthly_trends['Sales amount'].plot(kind = 'line' , color = 'blue' , marker = 'o')
pp.title('Monthly sales trend')
pp.ylabel('Sales amount')
pp.grid(True)

pp.subplot(3,1,2)
monthly_trends['profit'].plot(kind = 'line' , color = 'green' , marker = 'o')
pp.title('Monthly profit trend')
pp.ylabel('profit')
pp.grid(True)

pp.subplot(3,1,3)
monthly_trends['Order count'].plot(kind = 'line' , color = 'red' , marker = 'o')
pp.title('Monthly Order count trend')
pp.ylabel('Order count')
pp.grid(True)

pp.tight_layout()
pp.savefig('Monthly_trends.png')
pp.close()

#Advanced Analysis
print("...Correlation analysis...")

num_df = df[['Quantity' , 'Unit price' , 'discount(%)' , 'Sales amount' , 'profit']]

correlation_matrix = num_df.corr()
print("Correlation Matrix : ")
print(correlation_matrix, '\n\n')

pp.figure(figsize = (15,10))
sns.heatmap(correlation_matrix , annot = True , cmap = 'coolwarm' , center = 0 , square = True , linewidth = 0.5)
pp.title("Correlation Heatmap")
pp.tight_layout()
pp.savefig("correlation_matrix.png")
pp.close()


print("...Customer Id Analysis...")

seg_analysis = df.groupby('customer id').agg({
    'Sales amount' : ['sum' , 'mean'],
    'profit' : ['sum' , 'mean'],
    'Order id' : 'count',
    'discount(%)' : 'mean'
}).round(2)

seg_analysis.columns = ['Total sales', 'avg sales', 'Total profit', 'avg profit', 'Order count', 'avg discount']
print(seg_analysis, '\n\n')

fig, axes = pp.subplots(2, 2, figsize=(15, 10))

seg_analysis['Total sales'].plot(kind='bar', ax=axes[0,0], color='lightblue')
axes[0,0].set_title('Total sales by customer id')
axes[0,0].tick_params(axis='x', rotation=30)

seg_analysis['Total profit'].plot(kind='bar', ax=axes[0,1], color='lightgreen')
axes[0,1].set_title('Total profit by customer id')
axes[0,1].tick_params(axis='x', rotation=30)

seg_analysis['avg profit'].plot(kind='bar', ax=axes[1,0], color='orange')
axes[1,0].set_title('avg profit by customer id')
axes[1,0].tick_params(axis='x', rotation=30)

seg_analysis['avg discount'].plot(kind='bar', ax=axes[1,1], color='red')
axes[1,1].set_title('avg discount by customer id')
axes[1,1].tick_params(axis='x', rotation=30)

pp.tight_layout()
pp.savefig("customer_id.png")
pp.close()


#key insights and summary
print("...Key insights summary...")

#overall matrics
total_sales = df['Sales amount'].sum()
total_profit = df['profit'].sum()
total_orders = df['Order id'].nunique()
avg_profit_margin = (total_profit/total_sales) * 100

print(f"Overall performance : \n")
print(f"Total sales : ${total_sales: ,.2f}")
print(f"Total Profit : ${total_profit:,.2f}")
print(f"Total Orders : {total_orders}")
print(f"Average Profit Margin : {avg_profit_margin :.2f}%")

#top performance categories
top_categories = df.groupby('category')['profit'].sum().sort_values(ascending = False)
print(f"\nTop performing categories :\n")
for i , (category , profit) in enumerate(top_categories.items(), 1) :
    print(f"{i}. {category}: ${profit :,.2f}")

#regional performance
best_region = df.groupby('region')['profit'].sum().idxmax()
print(f"\nBest Performing Region : {best_region}")

#delivery performance
del_stats = df['Delivery status'].value_counts(normalize = True) * 100
print(f"\nDelivery Status : ")
for status , percentage in del_stats.items():
    print(f"{status} : {percentage:.1f}%")

#customer id
best_id = df.groupby('customer id')['profit'].sum().idxmax()
print(f"\nmost Profitable customer id : {best_id}")

#export results
analysis_results = {
    'total_sales' : total_sales,
    'total_profit' : total_profit,
    'total_orders' : total_orders,
    'average_profit_margin' : avg_profit_margin,
    'top_category' : top_categories.index[0],
    'best_region' : best_region,
    'best_id' : best_id
}

res_df = pd.DataFrame([analysis_results])
res_df.to_csv("eda analysis summary.csv" , index = False)
print("\n Analysis Summary saved to 'eda analysis summary.csv")
print(res_df)










