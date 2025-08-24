@@ -75,8 +75,8 @@
 def delete_task(task_id):
     """Delete a task from the list - INTENTIONAL BUG: Always deletes the last task"""
     if tasks:
-        # BUG: Instead of deleting the task at task_id, always delete the last task
-        tasks.pop()  # This should be: tasks.pop(task_id)
+        # Fixed: Delete the task at the specified task_id
+        tasks.pop(task_id)
     return redirect(url_for('index'))