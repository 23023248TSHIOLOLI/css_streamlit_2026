# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 13:52:06 2026

@author: Tshiololi Tshedza
"""

import streamlit as st
import datetime

# -----------------------------
# Initialize session state
# -----------------------------
if "users" not in st.session_state:
    st.session_state.users = {
        "admin": {
            "password": "1234",
            "balance": 1000.0,
            "transactions": []
        }
    }

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_user" not in st.session_state:
    st.session_state.current_user = None


# -----------------------------
# Helper Functions
# -----------------------------
def login(username, password):
    users = st.session_state.users
    if username in users and users[username]["password"] == password:
        st.session_state.logged_in = True
        st.session_state.current_user = username
        return True
    return False


def logout():
    st.session_state.logged_in = False
    st.session_state.current_user = None


def deposit(amount):
    user = st.session_state.current_user
    st.session_state.users[user]["balance"] += amount
    add_transaction("Deposit", amount)


def withdraw(amount):
    user = st.session_state.current_user
    if st.session_state.users[user]["balance"] >= amount:
        st.session_state.users[user]["balance"] -= amount
        add_transaction("Withdraw", amount)
        return True
    return False


def add_transaction(type_, amount):
    user = st.session_state.current_user
    transaction = {
        "type": type_,
        "amount": amount,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    st.session_state.users[user]["transactions"].append(transaction)


# -----------------------------
# App UI
# -----------------------------
st.title("🏦 Simple Banking App")

if not st.session_state.logged_in:
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(username, password):
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

else:
    user = st.session_state.current_user
    st.success(f"Welcome, {user}!")

    st.subheader("Account Balance")
    balance = st.session_state.users[user]["balance"]
    st.write(f"💰 Current Balance: ${balance:.2f}")

    st.subheader("Deposit Money")
    deposit_amount = st.number_input("Enter deposit amount", min_value=0.0, step=10.0)
    if st.button("Deposit"):
        if deposit_amount > 0:
            deposit(deposit_amount)
            st.success(f"${deposit_amount:.2f} deposited successfully!")

    st.subheader("Withdraw Money")
    withdraw_amount = st.number_input("Enter withdraw amount", min_value=0.0, step=10.0)
    if st.button("Withdraw"):
        if withdraw_amount > 0:
            if withdraw(withdraw_amount):
                st.success(f"${withdraw_amount:.2f} withdrawn successfully!")
            else:
                st.error("Insufficient balance!")

    st.subheader("Transaction History")
    transactions = st.session_state.users[user]["transactions"]

    if transactions:
        for txn in reversed(transactions):
            st.write(
                f"{txn['time']} | {txn['type']} | ${txn['amount']:.2f}"
            )
    else:
        st.info("No transactions yet.")

    if st.button("Logout"):
        logout()
        st.experimental_rerun()