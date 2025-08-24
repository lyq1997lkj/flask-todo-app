@@ -73,8 +73,8 @@
 @app.route('/delete/<int:task_id>', methods=['POST'])
 def delete_task(task_id):
     """Delete a task from the list - INTENTIONAL BUG: Always deletes the last task"""
-    if tasks:
-        # BUG: Instead of deleting the task at task_id, always delete the last task
-        tasks.pop()  # This should be: tasks.pop(task_id)
+    if 0 <= task_id < len(tasks):
+        # Fixed: Delete the task at the specified task_id
+        tasks.pop(task_id)
     return redirect(url_for('index'))