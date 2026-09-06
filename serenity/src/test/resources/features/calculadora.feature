Feature: Calculadora - Operaciones básicas
  Como usuario de la API de la calculadora
  Quiero poder sumar, restar, multiplicar y dividir dos números
  Para obtener resultados correctos con valores positivos y negativos

  Background:
    Given que la API de la calculadora está disponible

  # -------------------------------------------------------------------------
  Scenario Outline: Sumar dos números
    When el usuario suma <a> y <b>
    Then el resultado de la suma debe ser <resultado>

    Examples:
      | a   | b   | resultado |
      | 5   | 3   | 8         |
      | -5  | -3  | -8        |

  # -------------------------------------------------------------------------
  Scenario Outline: Restar dos números
    When el usuario resta <b> de <a>
    Then el resultado de la resta debe ser <resultado>

    Examples:
      | a   | b   | resultado |
      | 10  | 4   | 6         |
      | -10 | -4  | -6        |

  # -------------------------------------------------------------------------
  Scenario Outline: Multiplicar dos números
    When el usuario multiplica <a> por <b>
    Then el resultado de la multiplicación debe ser <resultado>

    Examples:
      | a   | b   | resultado |
      | 6   | 7   | 42        |
      | -6  | -7  | 42        |

  # -------------------------------------------------------------------------
  Scenario Outline: Dividir dos números
    When el usuario divide <a> entre <b>
    Then el resultado de la división debe ser <resultado>

    Examples:
      | a    | b   | resultado |
      | 20   | 5   | 4         |
      | -20  | -5  | 4         |

  # -------------------------------------------------------------------------
  Scenario: Dividir entre cero debe mostrar un error controlado
    When el usuario intenta dividir 20 entre 0
    Then la API debe responder con un error de división entre cero
