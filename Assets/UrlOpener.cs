using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class UrlOpener : MonoBehaviour
{
   public void Openurl()
    {
        Application.OpenURL("http://192.168.215.129:8501");
    }
}
