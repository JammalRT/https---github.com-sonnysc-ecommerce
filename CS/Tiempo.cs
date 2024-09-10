using System.Collections;
using UnityEngine;
using UnityEngine.UI;

public class TimeSkipSystem : MonoBehaviour
{
    public GameObject timeSkipMenu;
    public Slider timeSlider;
    public Text timeText; 
    public float timeScaleMultiplier = 100f; 
    public Animator playerAnimator; 

    private bool isTimeSkipping = false; 

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.T))
        {
            timeSkipMenu.SetActive(!timeSkipMenu.activeSelf);
        }

        if (isTimeSkipping)
        {
            Time.timeScale = timeScaleMultiplier; 
        }
        else
        {
            Time.timeScale = 1f; 
        }
    }

    public void StartTimeSkip()
    {
        isTimeSkipping = true;
        playerAnimator.SetBool("IsSitting", true); 
    }

    public void StopTimeSkip()
    {
        isTimeSkipping = false;
        playerAnimator.SetBool("IsSitting", false); 
    }
+
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
        timeSkipMenu.SetActive(false);
    }
}