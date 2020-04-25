# _*_ coding: utf-8 _*_

"""
from concurrent.futures import Future

future 未来对象，task的返回容器，包含线程任务已经完成或者正在进行的状态标记。

//python3\Lib\concurrent\futures\thread.py

但是， future是如何进入线程中的，看源码
    self._shutdown = threading.Lock()

    def submit(self, fn, *args, **kwargs):
        if self._shutdown:
            raise RuntimeError()
        f = _base.Future()
        w = _WorkItem(f, fn, args, kwargs)

        self._work_queue.put(w)
        self._adjust_thread_count()
        return f
    class _WorkItem(object):
    def __init__(self, future, fn, args, kwargs):
        self.future = future
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def run(self):
        if not self.future.set_running_or_notify_cancel():
            return

        try:
            result = self.fn(*self.args, **self.kwargs)
        except BaseException as exc:
            self.future.set_exception(exc)
            # Break a reference cycle with the exception 'exc'
            self = None
        else:
            self.future.set_result(result)

    def _adjust_thread_count(self):
        # When the executor gets lost, the weakref callback will wake up
        # the worker threads.
        def weakref_cb(_, q=self._work_queue):
            q.put(None)
        # TODO(bquinlan): Should avoid creating new threads if there are more
        # idle threads than items in the work queue.
        num_threads = len(self._threads)
        if num_threads < self._max_workers:
            thread_name = '%s_%d' % (self._thread_name_prefix or self,
                                     num_threads)
            t = threading.Thread(name=thread_name, target=_worker,
                                 args=(weakref.ref(self, weakref_cb),
                                       self._work_queue))
            t.daemon = True
            t.start()
            self._threads.add(t)
            _threads_queues[t] = self._work_queue
"""
from concurrent import futures