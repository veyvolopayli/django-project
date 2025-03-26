import dash
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests
from datetime import datetime

def get_nocodb_data():
    url = "http://backend:8000/nocodb-data/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            records = data.get('records', [])
            print("Полученные данные:", records)
            
            cleaned_records = []
            for record in records:
                clean_record = {
                    'ID': record.get('Id'),
                    'First Name': record.get('first_name'),
                    'Last Name': record.get('last_name'),
                    'Username': record.get('username'),
                    'Role': record.get('role'),
                    'Contact Info': record.get('contact_info'),
                    'Created At': record.get('CreatedAt'),
                    'Updated At': record.get('UpdatedAt'),
                    'Assets CSV': record.get('Asset_csvs'),
                    'Work Orders CSV': record.get('Work_Order_csvs')
                }
                cleaned_records.append(clean_record)
            
            return pd.DataFrame(cleaned_records)
        else:
            print("Ошибка при получении данных:", response.status_code)
            return pd.DataFrame()
    except Exception as e:
        print(f"Ошибка соединения: {e}")
        return pd.DataFrame()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('User Management Dashboard', style={'textAlign': 'center'}),
    dcc.Interval(
        id='interval-component',
        interval=1 * 1000,
        n_intervals=0,
        max_intervals=1
    ),
    html.Div(id='dashboard-content')
])

@app.callback(
    Output('dashboard-content', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_dashboard(n):
    df = get_nocodb_data()
    
    if df.empty:
        return html.Div([
            html.P('Нет данных для отображения.'),
            html.P('Проверьте соединение с NocoDB.')
        ], style={'textAlign': 'center'})

    try:
        df['Created At'] = pd.to_datetime(df['Created At']).dt.strftime('%Y-%m-%d %H:%M')
        df['Updated At'] = pd.to_datetime(df['Updated At']).dt.strftime('%Y-%m-%d %H:%M')
    except Exception as e:
        print(f"Ошибка преобразования дат: {e}")
    
    role_distribution = df['Role'].value_counts().reset_index()
    role_distribution.columns = ['Role', 'Count']
    
    fig_roles = px.pie(
        role_distribution,
        names='Role',
        values='Count',
        title='Распределение ролей пользователей',
        hole=0.3
    )
    
    columns = [
        {'name': 'ID', 'id': 'ID'},
        {'name': 'Имя', 'id': 'First Name'},
        {'name': 'Фамилия', 'id': 'Last Name'},
        {'name': 'Логин', 'id': 'Username'},
        {'name': 'Роль', 'id': 'Role'},
        {'name': 'Контакты', 'id': 'Contact Info'},
        {'name': 'Создан', 'id': 'Created At'},
        {'name': 'Обновлен', 'id': 'Updated At'},
        {'name': 'Ассеты CSV', 'id': 'Assets CSV'},
        {'name': 'Заказы CSV', 'id': 'Work Orders CSV'}
    ]
    
    return html.Div([
        html.Div([
            html.Div([
                html.H3('Статистика пользователей', className='text-center'),
                html.Hr(),
                html.P(f"Всего пользователей: {len(df)}"),
                html.P(f"Ролей в системе: {len(df['Role'].unique())}"),
                html.P(f"Последнее обновление: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
            ], className='card p-3 m-2'),
            
            html.Div([
                dcc.Graph(
                    figure=fig_roles,
                    config={'displayModeBar': False}
                )
            ], className='card p-3 m-2')
        ], className='row'),
        
        html.Div([
            html.H3('Детали пользователей', className='text-center mt-4'),
            dash_table.DataTable(
                data=df.to_dict('records'),
                columns=columns,
                style_table={
                    'overflowX': 'auto',
                    'maxHeight': '500px'
                },
                style_header={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'fontWeight': 'bold'
                },
                style_cell={
                    'textAlign': 'left',
                    'padding': '10px',
                    'whiteSpace': 'normal'
                },
                page_size=10
            )
        ], className='m-2')
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)