using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class FastTravelSystem : MonoBehaviour
{
    public List<Transform> fastTravelPoints; 
    public GameObject fastTravelMenu;
    private int currentPointIndex = 0;

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.M))
        {
            fastTravelMenu.SetActive(!fastTravelMenu.activeSelf);
        }
    }

    public void FastTravel(int pointIndex) 
    {
        if (pointIndex >= 0 && pointIndex < fastTravelPoints.Count)
        {
            Transform targetPoint = fastTravelPoints[pointIndex];
            GameObject player = GameObject.FindGameObjectWithTag("Player");
            player.transform.position = targetPoint.position; 


            fastTravelMenu.SetActive(false); 
        }
    }

    public void NextPoint()
    {
        currentPointIndex = (currentPointIndex + 1) % fastTravelPoints.Count;
    }

    public void PreviousPoint()
    {
        currentPointIndex--;
        if (currentPointIndex < 0)
            currentPointIndex = fastTravelPoints.Count - 1;
    }
}