from django.shortcuts import  HttpResponse


def task_create(request):
    return HttpResponse("""
        <html>
            <body>
                <h1>Create Task</h1>
                <form method="post">
                    <input type="text" name="task_name" placeholder="Task name">
                    <button type="submit">Create</button>
                </form>
            </body>
        </html>
    """)

