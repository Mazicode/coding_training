# from flask import Flask
# from celery import Celery
#
#
# def make_celery(app):
#     celery = Celery(app.import_name, broker=app.config["CELERY_BROKER_URL"],
#                     backend=app.config["CELERY_BACKEND_URL"])
#     celery.conf.update(app.config)
#     TaskBase = celery.Task
#
#     class ContextTask(TaskBase):
#         abstract = True
#
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return TaskBase.__call__(self, *args, **kwargs)
#
#     celery.Task = ContextTask
#     return celery
#
#
# app = Flask(__name__)
#
# app.config.update(
#     CELERY_BROKER_URL='"amqp://guest:guest@localhost:5672//"',
#     CELERY_RESULT_BACKEND='amqp'
# )
#
# celery = make_celery(app)
