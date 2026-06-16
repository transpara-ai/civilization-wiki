// compile/assets/civilizationOntology.js
// Pure contract for the Civilization arc. Browser (window.CivOntology) + Node (module.exports). No DOM.
(function (root) {
  "use strict";

  var STATUS_ORDER = ["future", "planned", "active", "done"];
  var SETTLED = { active: true, done: true };           // allowed left of "now"
  var NODE_TYPES = ["work", "goal", "order", "gate", "artifact", "surface",
    "actor", "phase", "event", "decision", "conflict",
    "policy", "invariant", "resource", "capability"];
  var PROVENANCE = ["reconstructed", "derived"];
  var STATUS_LANES = ["done", "active", "blocked", "planned", "future"];
  // Fixed lane order for the "gate" grouping, which lanes by gate FAMILY.
  // Lanes not in this list are appended alphabetically, before "(ungated)".
  var GATE_FAMILIES = [
    "v3.9 milestones (A-J)",
    "Deployment register (G-0..G-8.4)",
    "v4.0 (K/L)",
    "Release & security gates (v3.9)",
    "(ungated)",
  ];

  // "now" on the sequence axis = the frontier: the largest seq among settled (done/active) items.
  function deriveNow(items) {
    var now = -Infinity;
    for (var i = 0; i < items.length; i++) {
      if (!items[i]) continue;
      if (SETTLED[items[i].status] && items[i].seq > now) now = items[i].seq;
    }
    return now === -Infinity ? 0 : now;
  }

  function validateItems(items) {
    var errors = [];
    if (!Array.isArray(items)) return { ok: false, errors: ["items is not an array"] };
    var now = deriveNow(items);
    var seen = {};
    items.forEach(function (it, idx) {
      if (!it || typeof it !== "object") { errors.push("item[" + idx + "]: not an object"); return; }
      var where = "item[" + idx + "] " + (it.id ? it.id : "(no id)");
      if (!it.id) errors.push(where + ": missing id");
      else if (seen[it.id]) errors.push(where + ": duplicate id");
      else seen[it.id] = true;
      if (NODE_TYPES.indexOf(it.type) === -1) errors.push(where + ": invalid type '" + it.type + "'");
      if (STATUS_ORDER.indexOf(it.status) === -1) errors.push(where + ": invalid status '" + it.status + "'");
      if (PROVENANCE.indexOf(it.provenance) === -1) errors.push(where + ": invalid provenance '" + it.provenance + "'");
      if (typeof it.seq !== "number" || isNaN(it.seq)) errors.push(where + ": seq must be a number");
      if (!it.sprint) errors.push(where + ": missing sprint");
      if (!Array.isArray(it.repo)) errors.push(where + ": repo must be an array");
      if (typeof it.seq === "number" && !isNaN(it.seq) && it.seq < now && !SETTLED[it.status]) {
        errors.push(where + ": status '" + it.status + "' at seq " + it.seq +
          " is left of now (" + now + ") — past items must be done/active");
      }
    });
    return { ok: errors.length === 0, errors: errors };
  }

  function laneOf(it, dim) {
    if (dim === "status") return it.blocked ? "blocked" : it.status;
    if (dim === "repo") return (it.repo && it.repo[0]) || "(none)";
    if (dim === "sprint") return it.sprint || "(none)";
    if (dim === "gate") return it.family || "(ungated)";
    return "(none)";
  }
  function groupBy(items, dim) {
    var map = {}, order = [];
    items.forEach(function (it) {
      var lane = laneOf(it, dim);
      if (!map[lane]) { map[lane] = []; order.push(lane); }
      map[lane].push(it);
    });
    if (dim === "status") {
      order = STATUS_LANES.filter(function (l) { return map[l]; });
    } else if (dim === "gate") {
      // Order present lanes by GATE_FAMILIES; any lane not in that list is
      // appended alphabetically, immediately before "(ungated)".
      var known = GATE_FAMILIES.filter(function (l) { return map[l]; });
      var extras = order.filter(function (l) {
        return GATE_FAMILIES.indexOf(l) === -1;
      }).sort();
      var ungatedIdx = known.indexOf("(ungated)");
      if (ungatedIdx === -1) {
        order = known.concat(extras);
      } else {
        order = known.slice(0, ungatedIdx).concat(extras, known.slice(ungatedIdx));
      }
    } else {
      order.sort();
    }
    return order.map(function (l) { return { lane: l, items: map[l] }; });
  }

  function visibleDeps(items, selectedId) {
    if (!selectedId) return [];
    var edges = [];
    items.forEach(function (it) {
      (it.deps || []).forEach(function (from) {
        if (it.id === selectedId || from === selectedId) edges.push({ from: from, to: it.id });
      });
    });
    return edges;
  }

  var api = {
    STATUS_ORDER: STATUS_ORDER, NODE_TYPES: NODE_TYPES, PROVENANCE: PROVENANCE,
    SETTLED: SETTLED, deriveNow: deriveNow, validateItems: validateItems,
    groupBy: groupBy, visibleDeps: visibleDeps,
  };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  if (root) root.CivOntology = api;
})(typeof window !== "undefined" ? window : null);
