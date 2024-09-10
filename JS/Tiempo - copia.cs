using System.Collections;
using UnityEngine;
using UnityEngine.UI; // Necesario para manipular elementos de UI

public class TimeSkipSystem : MonoBehaviour
{
    public GameObject timeSkipMenu; // Panel del menú para elegir horas
    public Slider timeSlider; // Slider para seleccionar las horas
    public Text timeText; // Texto para mostrar las horas seleccionadas
    public float timeScaleMultiplier = 100f; // Factor de aceleración del tiempo
    public Animator playerAnimator; // Animator del personaje para la animación

    private bool isTimeSkipping = false; // Indica si se está adelantando el tiempo

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.T)) // Abre/cierra el menú con la tecla T
        {
            timeSkipMenu.SetActive(!timeSkipMenu.activeSelf);
        }

        if (isTimeSkipping)
        {
            Time.timeScale = timeScaleMultiplier; // Acelera el tiempo
        }
        else
        {
            Time.timeScale = 1f; // Tiempo normal
        }
    }

    public void StartTimeSkip()
    {
        isTimeSkipping = true;
        playerAnimator.SetBool("IsSitting", true); // Activa la animación de espera
    }

    public void StopTimeSkip()
    {
        isTimeSkipping = false;
        playerAnimator.SetBool("IsSitting", false); // Desactiva la animación
    }

    public void UpdateTimeText()
    {
        int hoursToSkip = (int)timeSlider.value;
        timeText.text = "Adelantar " + hoursToSkip + " horas";
    }

    public void SkipTime()
    {
        int hoursToSkip = (int)timeSlider.value;
        StartCoroutine(SkipTimeCoroutine(hoursToSkip));
    }

    IEnumerator SkipTimeCoroutine(int hours)
    {
        StartTimeSkip();

        float timePassed = 0f;
        while (timePassed < hours)
        {
            timePassed += Time.deltaTime * timeScaleMultiplier;
            yield return null;
        }

        StopTimeSkip();
        timeSkipMenu.SetActive(false); // Cierra el menú
    }
}