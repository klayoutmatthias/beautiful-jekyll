---
layout: page
---

# PCell Instances

This sample shows show to create PCell instances. It uses "TEXT" from the
"Basic" library which needs to be enabled by using `import klayout.lib`.

{: .box-note }
**Note**: The PCell parameters are specific for the kind of PCell. 
Code to list the parameters for all PCells from the "Basic" library can be downloaded here: [`list_pcell_parameters.py`](list_pcell_parameters.py).

Code:

```python
{% include_relative pcell_instances/pcell_instances.py %}
```

Result:

![Result](pcell_instances.png)

[Download GDS](pcell_instances.gds)

