package calculadora.stepdefinitions;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import io.restassured.response.Response;

import static net.serenitybdd.rest.SerenityRest.given;
import static org.assertj.core.api.Assertions.assertThat;

/**
 * Step definitions E2E para el feature calculadora.feature.
 *
 * Estas pruebas se ejecutan contra la API REST real (app.py) levantada
 * en http://localhost:5001. Cada paso arma la URL completa del
 * endpoint (no se depende de una baseURI global, que varia entre
 * versiones de Serenity/RestAssured), y valida codigo de estado y
 * cuerpo JSON de la respuesta real.
 *
 * Para ejecutar localmente:
 *   1) python app.py           (deja la API corriendo en :5001)
 *   2) mvn -f serenity/pom.xml clean verify   (desde la raiz del repo)
 */
public class CalculadoraStepDefinitions {

    private static final String BASE_URL = "http://localhost:5001";

    private Response respuesta;

    @Given("que la API de la calculadora está disponible")
    public void queLaApiEstaDisponible() {
        Response health = given().get(BASE_URL + "/");
        assertThat(health.getStatusCode()).isEqualTo(200);
    }

    @When("el usuario suma {double} y {double}")
    public void elUsuarioSuma(double a, double b) {
        respuesta = given().queryParam("a", a).queryParam("b", b).get(BASE_URL + "/sumar");
    }

    @When("el usuario resta {double} de {double}")
    public void elUsuarioResta(double b, double a) {
        respuesta = given().queryParam("a", a).queryParam("b", b).get(BASE_URL + "/restar");
    }

    @When("el usuario multiplica {double} por {double}")
    public void elUsuarioMultiplica(double a, double b) {
        respuesta = given().queryParam("a", a).queryParam("b", b).get(BASE_URL + "/multiplicar");
    }

    @When("el usuario divide {double} entre {double}")
    public void elUsuarioDivide(double a, double b) {
        respuesta = given().queryParam("a", a).queryParam("b", b).get(BASE_URL + "/dividir");
    }

    @When("el usuario intenta dividir {double} entre {double}")
    public void elUsuarioIntentaDividir(double a, double b) {
        respuesta = given().queryParam("a", a).queryParam("b", b).get(BASE_URL + "/dividir");
    }

    @Then("el resultado de la suma debe ser {double}")
    @Then("el resultado de la resta debe ser {double}")
    @Then("el resultado de la multiplicación debe ser {double}")
    @Then("el resultado de la división debe ser {double}")
    public void elResultadoDebeSer(double resultadoEsperado) {
        assertThat(respuesta.getStatusCode()).isEqualTo(200);
        assertThat(respuesta.jsonPath().getDouble("resultado")).isEqualTo(resultadoEsperado);
    }

    @Then("la API debe responder con un error de división entre cero")
    public void laApiDebeResponderConErrorDeDivisionEntreCero() {
        assertThat(respuesta.getStatusCode()).isEqualTo(400);
        assertThat(respuesta.jsonPath().getString("error")).containsIgnoringCase("cero");
    }
}
