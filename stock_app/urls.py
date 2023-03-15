from django.urls import path

from stock_app import views

urlpatterns = [
path("",views.index,name="index"),
path("dashboard",views.dashboard,name="dashboard"),
path("loginpage", views.loginpage, name="loginpage"),
path("logout_view", views.logout_view, name="logout_view"),


path("base", views.base, name="base"),
path("stock_add", views.stock_add, name="stock_add"),
path("stock_view", views.stock_view, name="stock_view"),
path("delete_stock_view/<int:id>/", views.delete_stock_view, name="delete_stock_view"),
path("update_stock_view/<int:id>/", views.update_stock_view, name="update_stock_view"),

path("customerbase", views.customerbase, name="customerbase"),
path("customers", views.customers, name="customers"),
path("customer_registration", views.customer_registration, name="customer_registration"),
path("customers_data", views.customers_data, name="customers_data"),
path("delete/<int:id>/", views.delete, name="delete"),
path("update/<int:id>/", views.update, name="update"),
path("customer_stock_view", views.customer_stock_view, name="customer_stock_view"),


]
