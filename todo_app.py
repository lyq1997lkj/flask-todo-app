@@ -67,7 +67,7 @@
 def delete_task(task_id):
     """Delete a task from the list - INTENTIONAL BUG: Always deletes the last task"""
     if tasks:
-        tasks.pop()  # This should be: tasks.pop(task_id)
+        tasks.pop(task_id)
     return redirect(url_for('index'))