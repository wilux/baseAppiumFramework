# content of login.feature

Feature: User login

    Scenario: User enters invalid email format
    When I tap on the login button
    And enter the credentials "test", "test"
    Then the email validation error message "Ingresa un correo válido o crea una cuenta" appears
