using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class FastTravelSystem : MonoBehaviour
{
    public List<Transform> fastTravelPoints; // Lista de puntos de viaje rápido
    public GameObject fastTravelMenu; // Panel del menú de viaje rápido
    private int currentPointIndex = 0; // Índice del punto actual

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.M)) // Abre/cierra el menú con la tecla M
        {
            fastTravelMenu.SetActive(!fastTravelMenu.activeSelf);
        }
    }

    public void FastTravel(int pointIndex) 
    {
        if (pointIndex >= 0 && pointIndex < fastTravelPoints.Count)
        {
            Transform targetPoint = fastTravelPoints[pointIndex];
            GameObject player = GameObject.FindGameObjectWithTag("Player"); // Encuentra al jugador
            player.transform.position = targetPoint.position; // Mueve al jugador

            // Opcional: Si cambias de escena al viajar, usa:
            // SceneManager.LoadScene(targetPoint.GetComponent<SceneReference>().ScenePath);

            fastTravelMenu.SetActive(false); // Cierra el menú
        }
    }

    // Métodos para navegar por el menú (Siguiente, Anterior, etc.)
    public void NextPoint()
    {
        currentPointIndex = (currentPointIndex + 1) % fastTravelPoints.Count;
        // Actualiza la interfaz del menú para mostrar el punto seleccionado
    }

    public void PreviousPoint()
    {
        currentPointIndex--;
        if (currentPointIndex < 0)
            currentPointIndex = fastTravelPoints.Count - 1;
        // Actualiza la interfaz del menú para mostrar el punto seleccionado
    }
}