import functools
import logging
import os

import dill
import ray
from tqdm import tqdm


def repeat(num_times, use_ray=False):
    """
    Decorator for calling a function multiple times.
    :param num_times: number of repeated calls
    :param use_ray: use Ray framework for multiprocessing
    :return: array of results
    """

    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.debug(f'Running function in parallel {num_times} times')
            results = []

            if use_ray:
                try:
                    ray.init()
                    # ray.init(dashboard_host='0.0.0.0', runtime_env={"working_dir": "/home/nkozlowski/phd",
                    #                                                 "excludes": ["*.dill", "*.pack"]})

                    remote_func = ray.remote(func)
                    feed = [remote_func.remote(*args, **kwargs) for _ in range(num_times)]
                    results = ray.get(feed)
                finally:
                    ray.shutdown()
            else:
                for _ in tqdm(range(num_times)):
                    results.append(func(*args, **kwargs))

            return results

        return wrapper

    return decorator_repeat


def get_from_cache_or_run(cache_path):
    """
    If a file exists at certain path it is loaded, otherwise the function is run
    :param cache_path: path to cache file
    :return: cached file or recomputed output
    """

    def decorator_cache(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)

            if os.path.exists(cache_path):
                logging.debug(f'Loading cache from file {cache_path}')
                with open(cache_path, 'rb') as f:
                    return dill.load(f)
            else:
                logging.debug(f'Recomputing function and saving the output to {cache_path}')
                res = func(*args, **kwargs)
                with open(cache_path, 'wb') as f:
                    dill.dump(res, f)

                return res

        return wrapper

    return decorator_cache
