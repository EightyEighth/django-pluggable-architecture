from stevedore import driver


def build_driver_api(namespace, name):
    driver_manager = driver.DriverManager(
        namespace=namespace,
        name=name,
        invoke_on_load=True
    )
    driver_instance = driver_manager.driver

    return driver_instance
