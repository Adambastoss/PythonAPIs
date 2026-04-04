#### Importing
**from flask import render_template**

#### Creating base.html file
Estructure html5 with tags...
<title>{% block title %} {% endblock %}</title>
<title>{% block title %} {% endblock %}</title>
`{% block title %} {% endblock %}`
`{% block content %} {% endblock %}`

#### `{% include %}` — inclusão direta de HTML
`{% include 'partials/navbar.html' %}`
`{% include 'partials/footer.html' %}`


#### `{%  import  %}` — reutilização de funções (macros)
Importa **macros (funções de template)** para reutilização.

*templates/macros.html*
{% macro render_user(user) %}
<tr>
    <td>{{ user.username }}</td>
    <td>{{ user.name }}</td>
</tr>
{% endmacro %}

*templates/arquivo_pra_usar_a_macro.html*
{% import 'macros.html' as macros %}

<table>
    {% for user in users %}
        {{ macros.render_user(user) }}
    {% endfor %}
</table>


#### Rendering db data in an html template
Python: `return render_template("users.html", context=users)`

</thead>

{% for user in context %}

<tr>

<td>{{ user.name }}</td>

<td>{{ user.username }}</td>

<td>{{ user.password }}</td>

</tr>

{% endfor %}

</table>

