package calculadora;

import io.cucumber.junit.CucumberOptions;
import net.serenitybdd.cucumber.CucumberWithSerenity;
import org.junit.runner.RunWith;

/**
 * Runner E2E con Serenity BDD + Cucumber (JUnit 4 clasico).
 *
 * Ejecuta todos los escenarios definidos en
 * src/test/resources/features/calculadora.feature contra la API REST
 * real de la calculadora (requiere que la API este corriendo en
 * http://localhost:5001, ver app.py).
 *
 * Comando (desde la raiz del repo): mvn -f serenity/pom.xml clean verify
 * Reporte HTML: serenity/target/site/serenity/index.html
 */
@RunWith(CucumberWithSerenity.class)
@CucumberOptions(
        features = "src/test/resources/features",
        glue = "calculadora.stepdefinitions"
)
public class CalculadoraTestSuite {
}
