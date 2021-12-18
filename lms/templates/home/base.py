<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bookstore - Simple is Better Than Complex</title>
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    {% include 'includes/header.html' %}
    <div class="container">
      {% block content %}
      {% endblock %}
    </div>
    <script src="{% static 'js/jquery-3.1.1.min.js' %}"></script>  <!-- JQUERY HERE -->
    <script src="{% static 'js/bootstrap.min.js' %}"></script>
    {% block javascript %}
    {% endblock %}
  </body>
</html>