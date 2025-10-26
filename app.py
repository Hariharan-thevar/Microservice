import streamlit as st

# In-memory data
if "users" not in st.session_state:
    st.session_state.users = [
        {"id": 1, "name": "Khushi", "email": "khushi@example.com"},
        {"id": 2, "name": "Karishma", "email": "karishma@example.com"}
    ]

if "orders" not in st.session_state:
    st.session_state.orders = [
        {"orderId": 101, "userId": 1, "product": "Laptop"},
        {"orderId": 102, "userId": 2, "product": "Phone"}
    ]

st.title("Microservice App")

menu = st.sidebar.selectbox("Go to", ["Home", "Users", "Orders"])

# ---- Home ----
if menu == "Home":
    st.subheader("Welcome to Microservice App")
    st.write("Use the sidebar to navigate between Users and Orders.")

# ---- Users ----
elif menu == "Users":
    st.subheader("Manage Users")
    
    with st.form("add_user"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        submitted = st.form_submit_button("Add User")
        if submitted:
            new_id = len(st.session_state.users) + 1
            st.session_state.users.append({"id": new_id, "name": name, "email": email})
            st.success(f"User {name} added!")

    st.write("### Current Users")
    st.table(st.session_state.users)

# ---- Orders ----
elif menu == "Orders":
    st.subheader("Manage Orders")
    
    with st.form("add_order"):
        user_options = {user["name"]: user["id"] for user in st.session_state.users}
        user_name = st.selectbox("Select User", list(user_options.keys()))
        product = st.text_input("Product Name")
        submitted = st.form_submit_button("Add Order")
        if submitted:
            new_id = 101 + len(st.session_state.orders)
            userId = user_options[user_name]
            st.session_state.orders.append({"orderId": new_id, "userId": userId, "product": product})
            st.success(f"Order {product} added for {user_name}!")

    st.write("### Current Orders")
    st.table(st.session_state.orders)
